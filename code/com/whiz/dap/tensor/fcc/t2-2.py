import pandas as pd
import tensorflow as tf

print(tf.__version__)
CSV_COLUMN_NAMES = ['SLength', 'SWidth', 'PLength', 'PWidth', 'Species']
SPECIES_CLASS = ['Setosa', 'Versicolor', 'Virginica']


def get_data(file_name):
    data_frame = pd.read_csv(file_name, names=CSV_COLUMN_NAMES, header=0)
    y = data_frame['Species']
    x = data_frame[['SLength', 'SWidth', 'PLength', 'PWidth']]
    return data_frame, y, x


train_data, train_y, train_x = get_data("./data/iris_training.csv")


def input_fn(features, labels, training=True, batch_size=256):
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle and repeat if you are in training mode.
    if training:
        dataset = dataset.shuffle(1000).repeat()

    return dataset.batch(batch_size)


def input_fn_for_preduct(features, batch_size=256):
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features)))

    return dataset.batch(batch_size)


def get_feature_columns():
    feature_columns = []
    for key in train_x.keys():
        feature_columns.append(tf.feature_column.numeric_column(key=key))

    return feature_columns


feature_columns = get_feature_columns()
print(feature_columns)

# Build a DNN with 2 hidden layers with 30 and 10 hidden nodes each.
classifier = tf.estimator.DNNClassifier(
    feature_columns=feature_columns,
    # Two hidden layers of 30 and 10 nodes respectively.
    hidden_units=[5, 10,10,5,10,10],
    # The model must choose between 3 classes.
    n_classes=3)

classifier.train(
    input_fn=lambda: input_fn(train_x, train_y, training=True),
    steps=5000)

# test modle from test data
test_data, test_y, test_x = get_data("./data/iris_test.csv")

eval_result = classifier.evaluate(input_fn=lambda: input_fn(test_x, test_y, training=False))
# 5.9	3	4.2	1.5 -> 1

test_data_frame = {'SLength': [5.9], 'SWidth': [3], 'PLength': [4.2], 'PWidth': [1.5]}
predictions = classifier.predict(input_fn=lambda:input_fn_for_preduct(test_data_frame))

for pred_dict in predictions:
    class_id = pred_dict['class_ids'][0]
    probability = pred_dict['probabilities'][class_id]

    print('Prediction is "{}" ({:.1f}%)'.format(
        SPECIES_CLASS[class_id], 100 * probability))