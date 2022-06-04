# spreads
spread_name_week = 'ALL Еженедельный Рабочий файл х5'
spread_name_month = 'ALL Ежемесячный Рабочий файл'
spread_name_month2 = 'ALL Пятерочка отдельно (для месяца)'
spread_name_hr = 'HR5'

# cfg
key = '97c890736dcf4412'
start_date = '2022-05-01'
delta = 31
month = True

# ids
car_id = '172904'
pyat_id = '160358'
per_id = '160394'
chizh_id = '233371'
x5_id = '174566'

# tags
car_t = '&tags=40 Карусель'
per_fast_t = '&tags=18.12_Перекресток быстро'
per_ru_t = '&tags=18.11_Впрок'
pyat_del_t = '&tags=18.11_ДоставкаПятерочка'
pyat_t = '&tags=40 Пятерочка'
chizh_t = '&tags=40_Чижик'
per_t = '&tags=40 Перекресток'
okolo = '&tags=19.10_Около'
omni = '&tags=14_Omni'
omni5 = '&tags=001_Omni'
log_15 = '&tags=15_Логистика'
log_1 = '&tags=001_Логистика'
hr = '&tags=001 HR'

# tags exclude
car_excl = '&excludeTags=15_Логистика&excludeTags=19.10_Около&excludeTags=14_Omni'
x5_excl = '&excludeTags=15_Логистика&excludeTags=19.10_Около&excludeTags=14_Omni&excludeTags=40 Карусель&excludeTags=40 Перекресток&excludeTags=40 Пятерочка&excludeTags=40_Чижик'
per_excl = '&excludeTags=18.11_Впрок&excludeTags=18.12_Перекресток быстро&excludeTags=15_Логистика&excludeTags=19.10_Около&excludeTags=14_Omni'
pyat_excl = '&excludeTags=18.11_ДоставкаПятерочка&excludeTags=15_Логистика&excludeTags=001_Логистика&excludeTags=19.10_Около&excludeTags=001_Omni'
x5_excl_m = '&excludeTags=15_Логистика&excludeTags=19.10_Около&excludeTags=14_Omni'

# config dict
configs = {
    # 'Карусель': {
    #     'car': [car_id, "", car_excl],
    #     'car_x5': [x5_id, car_t, x5_excl_m]
    # },
    # 'Доставка Пятерочка': {
    #     'pyat_del': [pyat_id, pyat_del_t, '']
    # },
    # 'Пятерочка': {
    #     'pyat': [pyat_id, "", pyat_excl],
    #     'pyat_x5': [x5_id, pyat_t, x5_excl_m]
    # },
    # 'Перекресток Быстро': {
    #     'pyat_del': [per_id, per_fast_t, ""]
    # },
    # 'Perekrestok.ru': {
    #     'pyat_del': [per_id, per_ru_t, ""]
    # },
    # 'Чижик': {
    #     'pyat': [chizh_id, "", ""],
    #     'pyat_x5': [x5_id, chizh_t, x5_excl_m]
    # },
    # 'X5': {
    #     'pyat_del': [x5_id, "", x5_excl]
    # },
    # 'Перекресток': {
    #     'pyat': [per_id, "", per_excl],
    #     'pyat_x5': [x5_id, per_t, x5_excl_m]
    # },
    # 'Omni': {
    #     'om_x5': [x5_id, omni, ""],
    #     'om_per': [per_id, omni, ""],
    #     'om_pyat': [pyat_id, omni5, ""],
    #     'om_car': [car_id, omni, ""]
    # },
    # 'Логистика': {
    #     'log_x5': [x5_id, log_15, ""],
    #     'log_per': [per_id, log_15, ""],
    #     'log_pyat1': [pyat_id, log_1, ""],
    #     'log_pyat15': [pyat_id, log_15, ""],
    #     'log_car': [car_id, log_15, ""]
    # },
    # 'HR': {
    #     'hr': [x5_id, hr, ""]
    # },
    # 'ОКОЛО': {
    #     'ok_x5': [x5_id, okolo, ""],
    #     'ok_per': [per_id, okolo, ""],
    #     'ok_pyat': [pyat_id, okolo, ""],
    #     'ok_car': [car_id, okolo, ""]
    # },
    'Data': {
        'pyat_hr': [pyat_id, hr, ""]
    }
}

# columns for df
columns = [
    'url', 'text', 'source', 'author.subscribers', 'city', 'region', 'author.name',
    'publicationPlace.name', 'author.url', 'publicationPlace.subscribers',
    'publicationPlace.url', 'sentiment', 'postType', 'engagement.engagement',
    'published', 'tags'
]

# new columns names for df
new_columns = {'url': 'Mentions Url',
               'text': 'Mentions Text',
               'source': 'Mentions Source',
               'author_subscribers': 'Mentions Author Subscribers',
               'city': 'Mentions City',
               'region': 'Mentions Region',
               'author.name': 'Mentions Author Name',
               'publicationPlace.name': 'Mentions Publicationplace Name',
               'author.url': 'Mentions Author Url',
               'publicationPlace.subscribers': 'Mentions Publicationplace Subscribers',
               'publicationPlace.url': 'Mentions Publicationplace Url',
               'sentiment': 'Mentions Sentiment',
               'postType': 'Mentions Posttype',
               'engagement.engagement': 'Mentions Engagement Engagement',
               'published': 'Mentions Published',
               'tags': 'Mentions Tags'
               }

# regions for hr
regions_dict = {
    'volga': ['Татарстан', 'Марий Эл', 'Чувашия', 'Ульяновская область',
              'Самарская область', 'Удмуртия'],

    'volga_sever': ['Ярославская область', 'Вологодская область', 'Костромская область',
                    'Ивановская область', 'Владимирская область', 'Кировская область',
                    'Республика Коми', 'Архангельская область', 'Нижегородская область',
                    'Мордовия'],

    'moskva': ['Москва'],

    'mo': ['Московская область'],

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

    'yuzhniy_ural': ['Челябинская область', 'Курганская область',
                     'Оренбургская область', 'Башкортостан'],

    'severniy_kavkaz': ['Краснодарский край', 'Армавирская область', 'Ставропольский край',
                        'Адыгея', 'Карачаево-Черкесия', 'Кабардино-Балкария',
                        'Республика Северная Осетия — Алания', 'Ингушетия',
                        'Чеченская Республика', 'Республика Дагестан', 'Калмыкия']
}
