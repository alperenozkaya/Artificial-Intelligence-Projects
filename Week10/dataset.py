import pandas as pd
data = pd.read_excel("CDR_MRI_without_outlier.xlsx")
print(data.head)

print(data["CDRGLOB"].value_counts())
print(data["NACCMMSE"].value_counts())

y = data["NACCMMSE"]
X = data["HIPPOVOL"]

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline


def PolynomialRegression(degree=2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree),
                         LinearRegression(**kwargs))


print(X.shape)
X[:, None].shape



import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # plot formatting
import numpy as np
Xmin = X.min()
Xmax = X.max()
X_test = np.linspace(Xmin, Xmax, 500)[:, None]


for degree in [1, 3, 5]:
    plt.scatter(X.ravel(), y, color='black')
    axis = plt.axis()
    y_test = PolynomialRegression(degree).fit(X[:, None], y).predict(X_test)
    plt.plot(X_test.ravel(), y_test, label='degree={0}'.format(degree))
    plt.show()
plt.xlim(-0.1, 1.0)
plt.ylim(-2, 12)
plt.legend(loc='best')
plt.show()

X2 = data[["HIPPOVOL","SEX","INDEPEND","NPISCORE"]]
print(X2)


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def PolynomialRidgeC(degree=4, **kwargs):
    return make_pipeline(PolynomialFeatures(degree),
                         RidgeClassifier(**kwargs))


y2 = pd.DataFrame(data["CDRGLOB"], dtype=str)

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# split the data with 50% in each set
X_train, X_test, y_train, y_test = train_test_split(X2, y2, stratify =y2, random_state=0,
                                  train_size=0.8)

model = PolynomialRidgeC(degree=3, alpha=0.01)
# fit the model on one set of data
model.fit(X_train, y_train)

# evaluate the model on the second set of data
y2_model = model.predict(X_test)
print(accuracy_score(y_test, y2_model))

y1_model = model.predict(X_train)
print(accuracy_score(y_train, y1_model))

test_dataset = []
train_dataset = []

for i in range(0, 7):
    model = PolynomialRidgeC(degree=i+5, alpha=0.01)

    model.fit(X_train, y_train)
    # evaluate the model on the second set of data
    y2_model = model.predict(X_test)
    test_dataset.append(accuracy_score(y_test, y2_model))

    y1_model = model.predict(X_train)
    train_dataset.append(accuracy_score(y_train, y1_model))


for i in range(0, 7):
    print("Test dataset accuracy with degree", i + 5, test_dataset[i])
    print("Train dataset accuracy with degree", i + 5, train_dataset[i])
    print()


import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import GridSearchCV

param_grid = {'polynomialfeatures__degree': np.arange(5, 12, 1),
              'ridgeclassifier__alpha': [0.000001, 0.00001, 0.00005, 0.0001, 0.0002, 0.0003],
             }

grid = GridSearchCV(PolynomialRidgeC(), param_grid, cv=7)
grid.fit(X_train, y_train)
print(grid.best_params_)

model = grid.best_estimator_
y_model = model.fit(X_train, y_train).predict(X_test)
print(accuracy_score(y_model, y_test))



