# Lets normalize all features, and remove the weather variables for the hour to be predicted.
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,LabelEncoder

class Normz:
    def __init__(self):
        self.reframed = pd.DataFrame()
    def s_to_super(self,data, n_in=1, n_out=1, dropnan=True):
        n_vars = 1 if type(data) is list else data.shape[1]
        df = pd.DataFrame(data)
        cols, names = list(), list()
        for i in range(n_in, 0, -1):
            cols.append(df.shift(i))
            names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
        for i in range(0, n_out):
            cols.append(df.shift(-i))
            if i == 0:
                names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
            else:
                names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
        agg = pd.concat(cols, axis=1)
        agg.columns = names
        if dropnan:
            agg.dropna(inplace=True)
        return agg


    def norml(self):
        # load dataset
        dataset = pd.read_csv('data/processed_data.csv', header=0, index_col=0)
        values = dataset.values
        encoder = LabelEncoder()
        values[:,4] = encoder.fit_transform(values[:,4])
        values = values.astype('float32')
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.scaled = self.scaler.fit_transform(values)
        self.reframed = self.s_to_super(self.scaled, 1, 1)
        # Dropping repeated columns, which we didn't want to predict
        self.reframed.drop(self.reframed.columns[[9,10,11,12,13,14,15]], axis=1, inplace=True)
        #print("** NOT REQUIRED DATA COLUMNS DROPPED **")
        print("#"*60)
        print("------ Data Before Normalizing ------")
        print(dataset.reset_index().drop(['date'],axis=1).head())
        #print(dataset.drop(['date']).head())
        print("------ Data After Normalizing ------")
        print(self.reframed.head())
        print("#"*50)
        return(self.reframed)

#
