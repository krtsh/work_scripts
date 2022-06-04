from functions import parse_data, dataframe_processing
import pandas as pd
from config import *

spread_name = 'ALL Еженедельный Рабочий файл х5'

if __name__ == '__main__':
    # Карусель
    print('Карусель started...')
    carousel = pd.DataFrame(parse_data(carousel_id,
                                       key,
                                       start_date,
                                       delta=delta,
                                       exclude_tags=carousel_exclude))
    print('X5 Карусель started...')
    X5_car = pd.DataFrame(parse_data(x5_id,
                                     key,
                                     start_date,
                                     delta=delta,
                                     tags='&tags=40 Карусель',
                                     exclude_tags=x5_exclude_))
    carousel_all = pd.concat([carousel, X5_car], axis=0)
    carousel_all.reset_index(inplace=True)
    dataframe_processing(carousel_all, spread_name, 'Карусель')

    # Доставка Пятерочка
    print('Доставка Пятерочка started...')
    delivery_5 = pd.DataFrame(parse_data(pyaterochka_id,
                                         key,
                                         start_date,
                                         delta=delta,
                                         tags=delivery_5_tags))
    dataframe_processing(delivery_5, spread_name, 'Доставка Пятерочка')

    # Пятерочка
    print('Пятерочка started...')
    pyaterochka = pd.DataFrame(parse_data(pyaterochka_id,
                                          key,
                                          start_date,
                                          delta=delta,
                                          exclude_tags=pyaterochka_exclude))
    print('X5 Пятерочка started...')
    X5_pyat = pd.DataFrame(parse_data(x5_id,
                                      key,
                                      start_date,
                                      delta=delta,
                                      tags='&tags=40 Пятерочка',
                                      exclude_tags=x5_exclude_))
    pyaterochka_all = pd.concat([pyaterochka, X5_pyat], axis=0)
    pyaterochka_all.reset_index(inplace=True)
    dataframe_processing(pyaterochka_all, spread_name, 'Пятерочка')

    # Перекресток Быстро
    print('Перекресток Быстро started...')
    perekrestok_fast = pd.DataFrame(parse_data(perekrestok_id,
                                               key,
                                               start_date,
                                               delta=delta,
                                               tags=perekrestok_fast_tags))
    dataframe_processing(perekrestok_fast, spread_name, 'Перекресток Быстро')

    # Perekrestok.ru
    print('Perekrestok.ru started...')
    perekrestok_ru = pd.DataFrame(parse_data(perekrestok_id,
                                             key,
                                             start_date,
                                             delta=delta,
                                             tags=perekrestok_ru_tags))
    dataframe_processing(perekrestok_ru, spread_name, 'Perekrestok.ru')

    # Чижик
    print('Чижик started...')
    chizhik = pd.DataFrame(parse_data(chizhik_id,
                                      key,
                                      start_date,
                                      delta=delta))
    print('X5 Чижик started...')
    X5_chizhik = pd.DataFrame(parse_data(x5_id,
                                         key,
                                         start_date,
                                         delta=delta,
                                         tags='&tags=40_Чижик',
                                         exclude_tags=x5_exclude_))
    chizhik_all = pd.concat([chizhik, X5_chizhik], axis=0)
    chizhik_all.reset_index(inplace=True)
    dataframe_processing(chizhik_all, spread_name, 'Чижик')

    # X5
    print('X5 started...')
    X5 = pd.DataFrame(parse_data(x5_id,
                                 key,
                                 start_date,
                                 delta=delta,
                                 exclude_tags=x5_exclude))
    dataframe_processing(X5, spread_name, 'X5')

    # Перекресток 
    print('Перекресток started...')
    perekrestok = pd.DataFrame(parse_data(perekrestok_id,
                                          key,
                                          start_date,
                                          delta=delta,
                                          exclude_tags=perekrestok_exclude))
    print('X5 Перекресток started...')
    X5_perekrestok = pd.DataFrame(parse_data(x5_id,
                                             key,
                                             start_date,
                                             delta=delta,
                                             tags='&tags=40 Перекресток',
                                             exclude_tags=x5_exclude_))
    perekrestok_all = pd.concat([perekrestok, X5_perekrestok], axis=0)
    perekrestok_all.reset_index(inplace=True)
    dataframe_processing(perekrestok_all, spread_name, 'Перекресток')

    # ОКОЛО
    print('ОКОЛО started...')
    print('ОКОЛО x5 started...')
    okolo_x5 = pd.DataFrame(parse_data(x5_id,
                                       key,
                                       start_date,
                                       delta=delta,
                                       tags=okolo))
    print('ОКОЛО perekrestok started...')
    okolo_per = pd.DataFrame(parse_data(perekrestok_id,
                                        key,
                                        start_date,
                                        delta=delta,
                                        tags=okolo))
    print('ОКОЛО pyaterochka started...')
    okolo_5 = pd.DataFrame(parse_data(pyaterochka_id,
                                      key,
                                      start_date,
                                      delta=delta,
                                      tags=okolo))
    print('ОКОЛО carousel started...')
    okolo_car = pd.DataFrame(parse_data(carousel_id,
                                        key,
                                        start_date,
                                        delta=delta,
                                        tags=okolo))
    okolo = pd.concat([okolo_5, okolo_car, okolo_x5, okolo_per], axis=0)
    okolo.reset_index(inplace=True)
    dataframe_processing(okolo, spread_name, 'ОКОЛО')

    # Omni
    print('Omni started...')
    print('Omni x5 started...')
    omni_x5 = pd.DataFrame(parse_data(x5_id,
                                      key,
                                      start_date,
                                      delta=delta,
                                      tags=omni))
    print('Omni perekrestok started...')
    omni_per = pd.DataFrame(parse_data(perekrestok_id,
                                       key,
                                       start_date,
                                       delta=delta,
                                       tags=omni))
    print('Omni pyaterochka started...')
    omni_5 = pd.DataFrame(parse_data(pyaterochka_id,
                                     key,
                                     start_date,
                                     delta=delta,
                                     tags=omni5))
    print('Onmi carousel started...')
    omni_car = pd.DataFrame(parse_data(carousel_id,
                                       key,
                                       start_date,
                                       delta=delta,
                                       tags=omni))
    omni = pd.concat([omni_5, omni_car, omni_x5, omni_per], axis=0)
    omni.reset_index(inplace=True)
    dataframe_processing(omni, spread_name, 'Omni')

    # Логистика
    print('Логистика started...')
    print('Логистика x5 started...')
    log_x5 = pd.DataFrame(parse_data(x5_id,
                                     key,
                                     start_date,
                                     delta=delta,
                                     tags=logistics))
    print('Логистика perekrestok started...')
    log_per = pd.DataFrame(parse_data(perekrestok_id,
                                      key,
                                      start_date,
                                      delta=delta,
                                      tags=logistics))
    print('Логистика 001 pyaterochka started...')
    log_51 = pd.DataFrame(parse_data(pyaterochka_id,
                                     key,
                                     start_date,
                                     delta=delta,
                                     tags='&tags=001_Логистика'))
    print('Логистика 15 pyaterochka started...')
    log_52 = pd.DataFrame(parse_data(pyaterochka_id,
                                     key,
                                     start_date,
                                     delta=delta,
                                     tags='&tags=15_Логистика'))
    print('Логистика carousel started...')
    log_car = pd.DataFrame(parse_data(carousel_id,
                                      key,
                                      start_date,
                                      delta=delta,
                                      tags=logistics))
    log = pd.concat([log_51, log_52, log_car, log_x5, log_per], axis=0)
    log.reset_index(inplace=True)
    dataframe_processing(log, spread_name, 'Логистика')

    # HR
    print('HR started...')
    print('HR x5 started...')
    hr_x5 = pd.DataFrame(parse_data(x5_id,
                                    key,
                                    start_date,
                                    delta=delta,
                                    tags=hr))
    print('HR x5 started...')
    dataframe_processing(hr_x5, spread_name, 'HR')
