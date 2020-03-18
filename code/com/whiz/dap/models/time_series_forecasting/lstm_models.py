import numpy as np
import matplotlib.pyplot as plt
import pandas
import math


from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import autocorrelation_plot
from sklearn.metrics import mean_squared_error

def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')

series = read_csv('./shampoo.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(series.head())
X = series.values
size = int(len(X) * 0.66)
train, test  = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()

import tensorflow as tf
print(tf.__version__)


series = read_csv('./shampoo.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(series.head())
X = series.values
size = int(len(X) * 0.66)
train, test  = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()



simple_lstm_model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(8, input_shape=1),
    tf.keras.layers.Dense(1)
])

simple_lstm_model.compile(optimizer='adam', loss='mae')
for t in range(len(test)):
    print(simple_lstm_model.predict(test[t]))
