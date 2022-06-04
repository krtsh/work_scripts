import config as cfg
import requests
import json
import pandas as pd
import gspread_pandas as gp
from datetime import date
from datetime import datetime
from datetime import timedelta
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from time import sleep


class DataProcessing:
    @staticmethod
    def parse_data(topic_id: str, apikey: str, start_date: str, tags="", exclude_tags="", delta=2, size=1000):
        start_date = date.fromisoformat(start_date)
        temp_data = []
        for i in range(delta):
            skip_size = 0
            print(start_date)
            while True:
                out = requests.get(
                    f'https://api.youscan.io/api/external/topics/{topic_id}'
                    f'/mentions?apiKey={apikey}'
                    f'&from={date.isoformat(start_date)}'
                    f'&to={date.isoformat(start_date)}'
                    f'&processed=true'
                    f'{tags}'
                    f'{exclude_tags}'
                    f'&skip={skip_size}'
                    f'&size={size}')

                if len(out.text) < 500:
                    print(out.text)
                    break
                temp_data += json.loads(out.text)['mentions']
                skip_size += 1000
                print(len(temp_data))
            start_date += timedelta(days=1)
            sleep(2)
        return temp_data

    @staticmethod
    def region_labels(x):
        if x in cfg.regions_dict['volga']:
            return 'Волга'
        elif x in cfg.regions_dict['volga_sever']:
            return 'Волга-Север'
        elif x in cfg.regions_dict['moskva']:
            return 'Москва'
        elif x in cfg.regions_dict['mo']:
            return 'Московская область'
        elif x in cfg.regions_dict['severniy_kavkaz']:
            return 'Северный Кавказ'
        elif x in cfg.regions_dict['severo_zapad']:
            return 'Северо-Запад'
        elif x in cfg.regions_dict['sibir']:
            return 'Сибирь'
        elif x in cfg.regions_dict['ural']:
            return 'Урал'
        elif x in cfg.regions_dict['centr']:
            return 'Центр'
        elif x in cfg.regions_dict['yug']:
            return 'Юг'
        elif x in cfg.regions_dict['yuzhniy_ural']:
            return 'Южный Урал'
        else:
            pass

    def dataframe_processing(self, dataframe, hr=False):
        # labels for hr report
        if hr:
            dataframe['Macro Region'] = dataframe['region'].apply(self.region_labels)
        # del last spaces
        dataframe['tags'] = dataframe.tags.apply(lambda x: [i.strip(' ') for i in x])
        # datetime
        dataframe['published'] = dataframe.published.apply(lambda x: (
                datetime.strptime(x.split('+')[0].split('.')[0], "%Y-%m-%dT%H:%M:%S") + timedelta(
            hours=3)).strftime("%Y-%m-%d"))
        # find and split tags
        frame_columns = ['tag_' + str(x) for x in range(dataframe.tags.apply(lambda x: len(x)).max())]
        tags_df = pd.DataFrame(dataframe.tags.to_list(), columns=frame_columns)
        dataframe = pd.concat([dataframe, tags_df], axis=1)
        dataframe.rename(columns=cfg.new_columns, inplace=True)
        return dataframe


class Sheets:
    c = ''
    gc = ''

    def connect(self, directory, file):
        self.c = gp.conf.get_config(conf_dir=directory, file_name=file)
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('google_secret.json', scope)
        self.gc = gspread.authorize(credentials)

    def upload_to_sheet(self, spread_name, sheet_name, dataframe):
        # clear old data
        sht = self.gc.open(spread_name)
        sht.values_clear(f"{sheet_name}!A1:X100000")
        print(f"{sheet_name} clear data")
        # write new data
        gp.Spread(spread_name, config=self.c).df_to_sheet(dataframe,
                                                          sheet=sheet_name,
                                                          start='A1',
                                                          index=False,
                                                          replace=False)
        print(f"{sheet_name} write data")
