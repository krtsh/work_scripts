import pandas as pd
import numpy as np
import pydantic

class YouScanProcessing:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def find_tags(tags, data, col_name):
        data[col_name] = ''
        for col in data.columns:
            if str(col).startswith(tags):
                data[col_name] += data[col].fillna('') + ', '
        data[col_name] = data[col_name].str.replace(' ,', '').str.strip(', ')
        data[col_name] = data[col_name].apply(lambda x: np.nan if x == '' else x)

    @staticmethod
    def tonality(data, elements, col_name):
        temp_dict = {}
        for element in elements:
            negative = data[(data[col_name] == element) & (data['Тональность'] == 'Негативная')]['Тональность'].count()
            neutral = data[(data[col_name] == element) & (data['Тональность'] == 'Нейтральная')]['Тональность'].count()
            positive = data[(data[col_name] == element) & (data['Тональность'] == 'Позитивная')]['Тональность'].count()
            total = sum([negative, neutral, positive])
            temp_dict[element] = [negative, neutral, positive, total]

        df = pd.DataFrame(temp_dict)
        df.rename(index={0: 'Negative', 1: 'Neutral', 2: 'Positive', 3: 'Total'}, inplace=True)
        df = df.transpose().sort_values(by=['Total'], ascending=False)

        return df

    @staticmethod
    def tonality_percent(data, total_types=True):
        if total_types:
        	data = data.append(data[['Negative', 'Neutral', 'Positive', 'Total']] \
                           .sum().to_frame().transpose().rename(index={0: 'Total types'}))

        data['Negative %'] = (data['Negative'] / data['Total'] * 100).round(2)
        data['Neutral %'] = (data['Neutral'] / data['Total'] * 100).round(2)
        data['Positive %'] = (data['Positive'] / data['Total'] * 100).round(2)

        return data

    @staticmethod
    def percent(data, 
    	total_types=True, 
    	calc_columns=[], 
    	percent_columns=[], 
    	div_round=0, 
    	to_percent=True):

        if total_types:
            data = data.append(data[calc_columns] \
                           .sum().to_frame().transpose() \
                           .rename(index={0: 'Total types'}))
        if to_percent:
        	multiplicator = 100
        else:
        	multiplicator = 1

        data[percent_columns[0]] = (data[calc_columns[0]] / 
        							data[calc_columns[3]] * 
        							multiplicator) \
        							.round(div_round)

        data[percent_columns[1]] = (data[calc_columns[1]] / 
        							data[calc_columns[3]] * 
        							multiplicator) \
        							.round(div_round)

        data[percent_columns[2]] = (data[calc_columns[2]] / 
        							data[calc_columns[3]] * 
        							multiplicator) \
        							.round(div_round)

        return data

    @staticmethod
    def nsi(data):
    	neg = data.query('Тональность == "Негативная"') \
    	          .groupby('Дата').agg({'Тональность': 'count'}) \
    	          .rename(columns={'Тональность':'Негативная'})

    	neu = data.query('Тональность == "Нейтральная"') \
    	          .groupby('Дата').agg({'Тональность': 'count'}) \
    	          .rename(columns={'Тональность':'Нейтральная'})

    	pos = data.query('Тональность == "Позитивная"') \
    	          .groupby('Дата').agg({'Тональность': 'count'}) \
    	          .rename(columns={'Тональность':'Позитивная'})

    	tot = data.groupby('Дата').agg({'Тональность': 'count'}) \
    	                          .rename(columns={'Тональность':'Итого'})

    	nsi = pd.concat([neg, neu, pos, tot],axis=1)
    	nsi = nsi.append(nsi.sum().to_frame() \
    	                          .transpose() \
    	                          .rename(index={0:'Итого'}))

    	nsi['NSI'] = ((nsi['Нейтральная'] + 
    	               nsi['Позитивная'] - 
    	               nsi['Негативная']) / 
    	               nsi['Итого']) \
    	               .round(2)

    	return nsi

    def rounding(num):
        if 999 < num < 1000000:
            return f'{round(num / 1000,1)}K'
        elif num > 1000000:
            return f'{round(num / 1000000,1)}M'
        else:
            return num

    def joining(data):
        return [(f'{data.loc[index][0].astype(int)} ({(data.loc[index][0] / data.sum()[0] * 100).round().astype(int)}%)') for index in data.index]