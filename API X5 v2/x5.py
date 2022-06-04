from functions import DataProcessing, Sheets
from pandas import json_normalize
import config as cfg

if __name__ == '__main__':
    worker = DataProcessing()
    loader = Sheets()
    connection = loader.connect('./', 'google_secret.json')

    for key, value in cfg.configs.items():
        output = []
        for name, data in value.items():
            print(key + ' ' + name + ' started...')
            output += worker.parse_data(data[0],
                                        cfg.key,
                                        cfg.start_date,
                                        data[1],
                                        data[2],
                                        delta=cfg.delta)
        if cfg.month:
            if key == 'Data':
                df = worker.dataframe_processing(json_normalize(output)[cfg.columns], hr=True)
            else:
                df = worker.dataframe_processing(json_normalize(output)[cfg.columns])
            match key:
                case 'X5' | 'Перекресток' | 'Perekrestok.ru' | 'Карусель' | 'Логистика':
                    loader.upload_to_sheet(cfg.spread_name_month, key, df)
                case 'Пятерочка' | 'Перекресток Быстро' | 'Доставка Пятерочка' | 'Чижик' | 'ОКОЛО' | 'Omni':
                    loader.upload_to_sheet(cfg.spread_name_month2, key, df)
                case 'Data':
                    loader.upload_to_sheet(cfg.spread_name_hr, key, df)
        elif key == 'Data':
            print('Not hr week')
            break
        else:
            df = worker.dataframe_processing(json_normalize(output)[cfg.columns])
            loader.upload_to_sheet(cfg.spread_name_week, key, df)
