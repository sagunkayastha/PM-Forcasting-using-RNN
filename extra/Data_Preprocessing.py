#from pandas import DataFrame, read_csv, concat
from datetime import datetime
import pandas as pd
class Dprepo:
	def parse(self,x):
		return datetime.strptime(x, '%Y %m %d %H')
	def __init__(self,data_name):
		dataset = pd.read_csv(data_name,  parse_dates = [['year', 'month', 'day', 'hour']], index_col=0, date_parser=self.parse)

		dataset.drop('No', axis=1, inplace=True)
		dataset.columns = ['PM', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain']
		dataset.index.name = 'date'
		dataset['PM'].fillna(0, inplace=True)
		dataset = dataset[24:]
		print(" -- \
		            Preprocessing Data\
		            --")
		print(" -- \
				Data Preview\
				  --")
		print(dataset.head(5))
		print("#"*60)

		dataset.to_csv('data/processed_data.csv')
