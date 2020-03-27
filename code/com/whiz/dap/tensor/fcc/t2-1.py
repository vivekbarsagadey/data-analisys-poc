import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import pandas as pd

print(tf.__version__)

# dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
# dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data

dftrain = pd.read_csv('./data/train.csv')  # training data
dfeval = pd.read_csv('./data/eval.csv')  # testing data
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

print(y_train.head())
print(y_eval.head())
print(dftrain.loc[0])
print(dftrain.shape)

CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
                       'embark_town', 'alone']
NUMERIC_COLUMNS = ['age', 'fare']

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
    vocabulary = dftrain[feature_name].unique()  # gets a list of all unique values from given feature column
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
    feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

print(feature_columns)


def input_fn(features, labels, num_epochs=10, shuffle=True, batch_size=256):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    if shuffle:
        dataset = dataset.shuffle(1000)

    return dataset.batch(batch_size).repeat(num_epochs)


linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)

linear_est.train(input_fn=lambda: input_fn(dftrain, y_train))  # train
result = linear_est.evaluate(input_fn=lambda: input_fn(dfeval, y_eval, num_epochs=1,
                                                       shuffle=False))  # get model metrics/stats by testing on tetsing data
pred_dicts = list(linear_est.predict(input_fn=lambda: input_fn(dfeval, y_eval, num_epochs=1,
                                                       shuffle=False)))
probs = pd.Series([pred['probabilities'][1] for pred in pred_dicts])

probs.plot(kind='hist', bins=20, title='predicted probabilities')
plt.show()
