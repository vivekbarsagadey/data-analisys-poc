# Import pandas
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Read in white wine data
white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv",
                    sep=';')

# Read in red wine data
red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')

# Define the scaler
scaler = StandardScaler().fit(X_train)

# Scale the train set
X_train = scaler.transform(X_train)

# Scale the test set
X_test = scaler.transform(X_test)


def show(red, white):
    fig, ax = plt.subplots(1, 2, figsize=(8, 4))

    ax[0].scatter(red['quality'], red["sulphates"], color="red")
    ax[1].scatter(white['quality'], white['sulphates'], color="white", edgecolors="black", lw=0.5)

    ax[0].set_title("Red Wine")
    ax[1].set_title("White Wine")
    ax[0].set_xlabel("Quality")
    ax[1].set_xlabel("Quality")
    ax[0].set_ylabel("Sulphates")
    ax[1].set_ylabel("Sulphates")
    ax[0].set_xlim([0, 10])
    ax[1].set_xlim([0, 10])
    ax[0].set_ylim([0, 2.5])
    ax[1].set_ylim([0, 2.5])
    fig.subplots_adjust(wspace=0.5)
    fig.suptitle("Wine Quality by Amount of Sulphates")

    plt.show()