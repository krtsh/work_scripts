from functions import parse_data, dataframe_processing
import pandas as pd
from config import key, pyaterochka_id

start_date = '2022-01-01'
delta = 31
spread_name = 'HR5'

print('Пятерочка started...')
pyaterochka_hr = pd.DataFrame(parse_data(pyaterochka_id,
                                         key,
                                         start_date,
                                         delta=delta,
                                         tags='&tags=001_HR'))
dataframe_processing(pyaterochka_hr, spread_name, 'Data', hr=True)
