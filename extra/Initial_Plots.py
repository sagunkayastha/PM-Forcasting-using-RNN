import matplotlib.pyplot as plt
import pandas as pd

class Init_Plot:
	def __init__(self):
		dataset = pd.read_csv('data/processed_data.csv', header=0, index_col=0)
		values = dataset.values
		groups = [0, 1, 2, 3, 5, 6, 7]
		i = 1
		plt.figure()
		for group in groups:
			plt.subplot(len(groups), 1, i)
			plt.plot(values[:, group],'b')
			plt.title(dataset.columns[group], y=0.5, loc='right')
			i += 1
		plt.show()
