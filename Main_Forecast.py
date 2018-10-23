# -*- coding: utf-8 -*-
"""
@author: sgnka

Code Based on
Multivariate Time Series Forecasting with LSTMs in Keras, by Jason Brownlee
https://machinelearningmastery.com
"""

from utils import *
from keras.models import Sequential
from keras.layers import CuDNNLSTM, LSTM
from keras.layers import Dense, Dropout
import matplotlib.pyplot as plt

input_filename = 'data/data.csv'

DP= Dprepo(input_filename)  #Calling Preprocessing function from Data_Preprocessing
plotting = Init_Plot()
Model_Data= Normz()

values = Model_Data.norml().values
n_train_hours = 365 * 24
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]

# Test Train Split
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]

train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))

print("------ Train/Test Split ------")
print(" Training data shape X, y => ",train_X.shape, train_y.shape,"\n Testing  data shape X, y => ", test_X.shape, test_y.shape)
print("#"*50)

# Model Building
model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dropout(0.3))
model.add(Dense(1,kernel_initializer='normal', activation='sigmoid'))
model.compile(loss='mae', optimizer='adam')
Model_out = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)

# Training_Test_Plots
plt.plot(Model_out.history['loss'], 'b', label='training history')
plt.plot(Model_out.history['val_loss'],  'r',label='testing history')
plt.title("Train and Test Loss for the LSTM")
plt.legend()
plt.show()
