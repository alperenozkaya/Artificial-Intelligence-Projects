import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB  # 1. choose model class
from sklearn.metrics import accuracy_score


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
    #plt.show()

    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y_iris,
                                                    random_state=1)

    model = GaussianNB()  # 2. instantiate model
    model.fit(Xtrain, ytrain)  # 3. fit model to data
    y_model = model.predict(Xtest)  # 4. predict on new data

    print(accuracy_score(ytest, y_model))


iris = load_iris()
iris = sns.load_dataset('iris')

print("Enter a feature:")
feature = str(input())
print("Enter an estimator:")
estimator = str(input())

plot_estimator(feature, estimator)







