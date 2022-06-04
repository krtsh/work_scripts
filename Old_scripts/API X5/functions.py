import sys
import requests
import json
from pydantic import BaseModel
import numpy as np
import copy
from bs4 import BeautifulSoup
import pandas as pd
import gspread_pandas as gp
from datetime import datetime, date, timedelta
# from datetime import datetime
# from datetime import timedelta
import time
# from config import regions_dict
from oauth2client.service_account import ServiceAccountCredentials
import gspread

sys.path.append('./')
c = gp.conf.get_config(conf_dir='./',
                       file_name='google_secret.json')
# spread = gp.Spread(spread_name, config=c)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('google_secret.json', scope)
gc = gspread.authorize(credentials)

dict_schema = {
    'id': [],
    'seq': [],
    'published': [],
    'addedAt': [],
    'url': [],
    'title': [],
    'text': [],
    'imageUrl': [],
    'source': [],
    'author_name': [],
    'author_avatarurl': [],
    'author_url': [],
    'author_gender': [],
    'author_age': [],
    'author_subscribers': [],
    'publicationPlace_name': [],
    'publicationPlace_avatarurl': [],
    'publicationPlace_url': [],
    'publicationPlace_gender': [],
    'publicationPlace_subscribers': [],
    'sentiment': [],
    'resourceType': [],
    'imageObjects': [],
    'imageScenes': [],
    'postType': [],
    'tags': [],
    'rating': [],
    'autoCategories': [],
    'starred': [],
    'engagement_likes': [],
    'engagement_engagement': [],
    'engagement_comments': [],
    'engagement_reposts': [],
    'engagement_views': [],
    'engagement_engagementRate': [],
    'engagement_dateCollected': [],
    'engagement_reactionsTotal': [],
    'postId': [],
    'parentPostId': [],
    'discussionId': [],
    'country': [],
    'region': [],
    'city': []
}

columns = [
    'url', 'text', 'source', 'author_subscribers', 'city', 'region', 'author_name',
    'publicationPlace_name', 'author_url', 'publicationPlace_subscribers',
    'publicationPlace_url', 'sentiment', 'postType', 'engagement_engagement',
    'published', 'tags'
]
new_columns = {'url': 'Mentions Url',
               'text': 'Mentions Text',
               'source': 'Mentions Source',
               'author_subscribers': 'Mentions Author Subscribers',
               'city': 'Mentions City',
               'region': 'Mentions Region',
               'author_name': 'Mentions Author Name',
               'publicationPlace_name': 'Mentions Publicationplace Name',
               'author_url': 'Mentions Author Url',
               'publicationPlace_subscribers': 'Mentions Publicationplace Subscribers',
               'publicationPlace_url': 'Mentions Publicationplace Url',
               'sentiment': 'Mentions Sentiment',
               'postType': 'Mentions Posttype',
               'engagement_engagement': 'Mentions Engagement Engagement',
               'published': 'Mentions Published',
               'tags': 'Mentions Tags'
               }

regions_dict = {
    'volga': ['Татарстан', 'Марий Эл', 'Чувашия', 'Ульяновская область',
              'Самарская область', 'Удмуртия'],

    'volga_sever': ['Ярославская область', 'Вологодская область', 'Костромская область',
                    'Ивановская область', 'Владимирская область', 'Кировская область',
                    'Республика Коми', 'Архангельская область', 'Нижегородская область',
                    'Мордовия'],

    'moskva': ['Москва', 'Московская область'],

    'severo_zapad': ['Санкт-Петербург', 'Ленинградская область', 'Псковская область',
                     'Мурманская область', 'Республика Карелия', 'Калининградская область',
                     'Новгородская область', 'Тверская область'],

    'sibir': ['Новосибирская область', 'Омская область', 'Алтайский край',
              'Кемеровская область', 'Томская область', 'Красноярский край',
              'Республика Хакасия'],

    'ural': ['Ханты-Мансийский автономный округ — Югра', 'Пермский край', 'Томская область',
             'Ямало-Ненецкий автономный округ', 'Свердловская область', 'Тюменская область'],

    'centr': ['Рязанская область', 'Тамбовская область', 'Тульская область', 'Липецкая область',
              'Воронежская область', 'Орловская область', 'Курская область', 'Белгородская область',
              'Калужская область', 'Смоленская область', 'Брянская область'],

    'yug': ['Ростовская область', 'Астраханская область', 'Волгоградская область',
            'Саратовская область', 'Пензенская область'],

    'yuzhniy_ural': ['Челябинская область', 'Курганская область', 'Оренбургская область', 'Башкортостан'],

    'severniy_kavkaz': ['Краснодарский край', 'Армавирская область', 'Ставропольский край', 'Адыгея',
                        'Карачаево-Черкесия', 'Кабардино-Балкария', 'Республика Северная Осетия — Алания',
                        'Ингушетия', 'Чеченская Республика', 'Республика Дагестан', 'Калмыкия']
}


class Engage(BaseModel):
    likes: int = np.nan
    comments: int = np.nan
    reposts: int = np.nan
    views: int = np.nan
    engagementRate: float = np.nan
    engagement: int = np.nan
    dateCollected: str = ''
    reactionsTotal: int = np.nan


class Author(BaseModel):
    name: str = ''
    avatarUrl: str = ''
    url: str = ''
    gender: str = ''
    age: int = np.nan
    subscribers: int = np.nan


class PublicationPlace(BaseModel):
    name: str = ''
    avatarUrl: str = ''
    url: str = ''
    gender: str = ''
    subscribers: int = np.nan


class Mentions(BaseModel):
    id: str = ''
    seq: int = np.nan
    published: str = ''
    addedAt: str = ''
    url: str = ''
    title: str = ''
    text: str = ''
    imageUrl: str = ''
    source: str = ''
    author: Author = None
    publicationPlace: PublicationPlace = None
    sentiment: str = ''
    resourceType: str = ''
    imageObjects: list[str] = ['']
    imageScenes: list[str] = ['']
    postType: str = ''
    tags: list[str] = ['']
    rating: float = np.nan
    autoCategories: list[str] = ['']
    starred: bool = None
    engagement: Engage = None
    postId: str = ''
    parentPostId: str = ''
    discussionId: str = ''
    country: str = ''
    region: str = ''
    city: str = ''


class Req(BaseModel):
    total: int = np.nan
    lastSeq: int = np.nan
    mentions: list[Mentions] = ['']


def parse_data(topic_id, apikey, start_date, delta=1, tags="", exclude_tags="", size=1000):
    start_date = date.fromisoformat(start_date)
    test_dict = copy.deepcopy(dict_schema)

    for d in range(delta):
        skip_size = 0
        print(start_date)
        while True:
            re = requests.get(
                f'https://api.youscan.io/api/external/topics/{topic_id}'
                f'/mentions?apiKey={apikey}'
                f'&from={date.isoformat(start_date)}'
                f'&to={date.isoformat(start_date)}'
                f'&processed=true'
                f'{tags}'
                f'{exclude_tags}'
                f'&skip={skip_size}'
                f'&size={size}')
            data = json.loads(re.text)
            skip_size += 1000
            if data.get('message') or len(data.get('mentions')) == 0:
                print(data.get('message'))
                break
            print(len(data.get('mentions')))
            res = Req.parse_raw(json.dumps(data))
            for i in res.mentions:
                test_dict['id'].append(i.id)
                test_dict['seq'].append(i.seq)
                test_dict['published'].append((datetime.strptime(i.published.split('+')[0].split('.')[0],
                                                                 "%Y-%m-%dT%H:%M:%S") + timedelta(hours=3))
                                              .strftime("%Y-%m-%d"))
                test_dict['addedAt'].append(i.addedAt)
                test_dict['url'].append(i.url)
                test_dict['title'].append(i.title)
                test_dict['text'].append(i.text)
                test_dict['imageUrl'].append(i.imageUrl)
                test_dict['source'].append(i.source)
                test_dict['sentiment'].append(i.sentiment)
                test_dict['resourceType'].append(i.resourceType)
                test_dict['imageObjects'].append(i.imageObjects)
                test_dict['imageScenes'].append(i.imageScenes)
                test_dict['postType'].append(i.postType)
                test_dict['tags'].append(i.tags)
                test_dict['rating'].append(i.rating)
                test_dict['autoCategories'].append(i.autoCategories)
                test_dict['starred'].append(i.starred)
                test_dict['postId'].append(i.postId)
                test_dict['parentPostId'].append(i.parentPostId)
                test_dict['discussionId'].append(i.discussionId)
                test_dict['country'].append(i.country)
                test_dict['city'].append(i.city)
                test_dict['region'].append(i.region)

                if i.publicationPlace is None or i.author is None or i.engagement is None:
                    test_dict['author_name'].append('')
                    test_dict['author_avatarurl'].append('')
                    test_dict['author_url'].append('')
                    test_dict['author_gender'].append('')
                    test_dict['author_age'].append(np.nan)
                    test_dict['author_subscribers'].append(np.nan)

                    test_dict['publicationPlace_name'].append('')
                    test_dict['publicationPlace_avatarurl'].append(np.nan)
                    test_dict['publicationPlace_url'].append('')
                    test_dict['publicationPlace_gender'].append('')
                    test_dict['publicationPlace_subscribers'].append(np.nan)

                    test_dict['engagement_likes'].append(np.nan)
                    test_dict['engagement_engagement'].append(np.nan)
                    test_dict['engagement_comments'].append(np.nan)
                    test_dict['engagement_reposts'].append(np.nan)
                    test_dict['engagement_views'].append(np.nan)
                    test_dict['engagement_engagementRate'].append(np.nan)
                    test_dict['engagement_dateCollected'].append('')
                    test_dict['engagement_reactionsTotal'].append(np.nan)
                else:
                    test_dict['author_name'].append(i.author.name)
                    test_dict['author_avatarurl'].append(i.author.avatarUrl)
                    test_dict['author_url'].append(i.author.url)
                    test_dict['author_gender'].append(i.author.gender)
                    test_dict['author_age'].append(i.author.age)
                    test_dict['author_subscribers'].append(i.author.subscribers)

                    test_dict['publicationPlace_name'].append(i.publicationPlace.name)
                    test_dict['publicationPlace_avatarurl'].append(i.publicationPlace.avatarUrl)
                    test_dict['publicationPlace_url'].append(i.publicationPlace.url)
                    test_dict['publicationPlace_gender'].append(i.publicationPlace.gender)
                    test_dict['publicationPlace_subscribers'].append(i.publicationPlace.subscribers)

                    test_dict['engagement_likes'].append(i.engagement.likes)
                    test_dict['engagement_engagement'].append(i.engagement.engagement)
                    test_dict['engagement_comments'].append(i.engagement.comments)
                    test_dict['engagement_reposts'].append(i.engagement.reposts)
                    test_dict['engagement_views'].append(i.engagement.views)
                    test_dict['engagement_engagementRate'].append(i.engagement.engagementRate)
                    test_dict['engagement_dateCollected'].append(i.engagement.dateCollected)
                    test_dict['engagement_reactionsTotal'].append(i.engagement.reactionsTotal)
        time.sleep(3)
        start_date += timedelta(days=1)
    return test_dict


def region_lables(x):
    if x in regions_dict['volga']:
        return 'Волга'
    elif x in regions_dict['volga_sever']:
        return 'Волга-Север'
    elif x in regions_dict['moskva']:
        return 'Москва'
    elif x in regions_dict['severniy_kavkaz']:
        return 'Северный Кавказ'
    elif x in regions_dict['severo_zapad']:
        return 'Северо-Запад'
    elif x in regions_dict['sibir']:
        return 'Сибирь'
    elif x in regions_dict['ural']:
        return 'Урал'
    elif x in regions_dict['centr']:
        return 'Центр'
    elif x in regions_dict['yug']:
        return 'Юг'
    elif x in regions_dict['yuzhniy_ural']:
        return 'Южный Урал'
    else:
        pass


def text_processing(text):
    return BeautifulSoup(text.replace('&#xA;', ' '), "lxml") \
        .get_text(strip=False).replace('\r', ' ').replace('\n', ' ')


def dataframe_processing(dataframe, spread_name, sheet_name, replace=False, hr=False):
    pd.options.mode.chained_assignment = None
    dataframe = dataframe[columns]  # pick columns
    # dataframe['text'] = dataframe.text \
    #     .apply(text_processing)

    # lables for hr report
    if hr:
        dataframe['Macro Region'] = dataframe['region'].apply(region_lables)

    dataframe['tags'] = dataframe.tags.apply(lambda x: [i.strip(' ') for i in x])  # del last spaces
    # find and split tags
    frame_columns = ['tag_' + str(x) for x in range(dataframe.tags.apply(lambda x: len(x)).max())]
    tags_df = pd.DataFrame(dataframe.tags.to_list(),
                           columns=frame_columns)

    dataframe = pd.concat([dataframe, tags_df], axis=1)
    dataframe.rename(columns=new_columns,
                     inplace=True)
    # clear old data
    sht = gc.open(spread_name)
    sht.values_clear(f"{sheet_name}!A1:X100000")
    print(f"{sheet_name} clear data")
    # write new data
    gp.Spread(spread_name,
              config=c).df_to_sheet(dataframe,
                                    sheet=sheet_name,
                                    start='A1',
                                    index=False,
                                    replace=replace)
    print(f"{sheet_name} write data")
