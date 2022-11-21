import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def plot_estimator(chosen_feature, estimator_feature):  # for petal length

    X_iris = iris.drop('species', axis=1)

    y_iris = X_iris[chosen_feature]

    X = X_iris[estimator_feature]
    y = y_iris

    X = np.array(X).reshape(-1, 1)

    model = LinearRegression(fit_intercept=False)
    #print(model)
    model.fit(X, y)

    xfit = np.linspace(0, 3)
    Xfit = xfit[:, np.newaxis]
    yfit = model.predict(Xfit)

    plt.scatter(X, y)
    plt.plot(xfit, yfit)
    plt.ylabel(chosen_feature)
    plt.xlabel(estimator_feature)
    plt.show()


iris = load_iris()
iris = sns.load_dataset('iris')

print("Enter a feature:")
feature = str(input())
print("Enter an estimator:")
estimator = str(input())

plot_estimator(feature, estimator)



