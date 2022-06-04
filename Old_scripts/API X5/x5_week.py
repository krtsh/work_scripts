from functions import parse_data, dataframe_processing
import pandas as pd
from config import *

spread_name = 'X5 06.2021'

if __name__ == '__main__':
    # # Данные для Карусели НЕДЕЛЯ / МЕСЯЦ
    # carousel = pd.DataFrame(parse_data(carousel_id,
    #                                 key,
    #                                 start_date,
    #                                 delta=delta))
    # dataframe_processing(carousel, 
    #                     'Данные для Карусели НЕДЕЛЯ / МЕСЯЦ')

    # # Данные для Доставка Пятерочка НЕДЕЛЯ / МЕСЯЦ
    # delivery_5 = pd.DataFrame(parse_data(pyaterochka_id,
    #                                     key,
    #                                     start_date,
    #                                     delta=delta,
    #                                     tags=delivery_5_tags))
    # dataframe_processing(delivery_5, 
    #                     'Данные для Доставка Пятерочка НЕДЕЛЯ / МЕСЯЦ')

    # Данные для Пятерочки НЕДЕЛЯ / МЕСЯЦ - обнуление листов2
    pyaterochka_obn = pd.DataFrame(parse_data(pyaterochka_id,
                                            key,
                                            start_date,
                                            delta=delta,
                                            exclude_tags=pyaterochka_exclude))
    dataframe_processing(pyaterochka_obn, spread_name,
                        'Данные для Пятерочки НЕДЕЛЯ / МЕСЯЦ - обнуление листов2')

    # # Данные для Перекресток Быстро НЕДЕЛЯ / МЕСЯЦ
    # perekrestok_fast = pd.DataFrame(parse_data(perekrestok_id,
    #                                         key,
    #                                         start_date,
    #                                         delta=delta,
    #                                         tags=perekrestok_fast_tags))
    # dataframe_processing(perekrestok_fast, 
    #                     'Данные для Перекресток Быстро НЕДЕЛЯ / МЕСЯЦ')

    # # Данные для Perekrestok.ru НЕДЕЛЯ / МЕСЯЦ
    # perekrestok_ru = pd.DataFrame(parse_data(perekrestok_id,
    #                                         key,
    #                                         start_date,
    #                                         delta=delta,
    #                                         tags=perekrestok_ru_tags))
    # dataframe_processing(perekrestok_ru, 
    #                     'Данные для Perekrestok.ru НЕДЕЛЯ / МЕСЯЦ')

    # # Данные для Чижика НЕДЕЛЯ / МЕСЯЦ
    # chizhik = pd.DataFrame(parse_data(chizhik_id,
    #                                 key,
    #                                 start_date,
    #                                 delta=delta))
    # dataframe_processing(chizhik, 
    #                     'Данные для Чижика НЕДЕЛЯ / МЕСЯЦ')

    # # Данные для Х5 НЕДЕЛЯ / МЕСЯЦ
    # X5 = pd.DataFrame(parse_data(x5_id,
    #                             key,
    #                             start_date,
    #                             delta=delta))
    # dataframe_processing(X5, 
    #                     'Данные для Х5 НЕДЕЛЯ / МЕСЯЦ')

    # # Данные для Перекрестка НЕДЕЛЯ / МЕСЯЦ
    # perekrestok = pd.DataFrame(parse_data(perekrestok_id,
    #                                     key,
    #                                     start_date,
    #                                     delta=delta,
    #                                     exclude_tags=perekrestok_exclude))
    # dataframe_processing(perekrestok, 
    #                     'Данные для Перекрестка НЕДЕЛЯ / МЕСЯЦ')

    # # Данные для Пятерочки
    # pyaterochka = pd.DataFrame(parse_data(pyaterochka_id,
    #                                     key,
    #                                     start_date,
    #                                     delta=delta))
    # dataframe_processing(pyaterochka, 
    #                     'Данные для Пятерочки')


