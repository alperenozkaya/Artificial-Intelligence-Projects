import seaborn as sns
import numpy as np
from sklearn.naive_bayes import GaussianNB # 1. choose model class
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report


def classification(feature):
    iris = sns.load_dataset('iris')
    classifier = ''

    if feature == 1:
        classifier = 'petal_length'
    elif feature == 2:
        classifier = 'petal_width'
    elif feature == 3:
        classifier = 'sepal_length'
    elif feature == 4:
        classifier = 'sepal_width'
    else:
        quit()

    X_iris = iris[classifier]  # feature that is used in the classification model
    X_iris = np.array(X_iris).reshape(-1, 1)
    y_iris = iris['species']  # target feature 'species'

    Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris,
                                                    random_state=1)
    model = GaussianNB()
    model.fit(Xtrain, ytrain)
    y_model = model.predict(Xtest)

    print('The accuracy score is:', accuracy_score(ytest, y_model))  # shows the accuracy of used model
    print('\nCLASSIFICATION MODEL\n')
    print(classification_report(ytest, y_model))  # prints the classification report

    mat = confusion_matrix(ytest, y_model)  # confusion matrix to illustrate the model's predictions
                                            # 0:setosa 1:versicolor 2:virginica
    sns.heatmap(mat, square=True, annot=True, cbar=False)

    plt.xlabel('Predicted species')
    plt.ylabel('True species ')
    plt.plot()
    plt.show()  # show the heat map


print('Enter a number for classification 1:petal_length 2:petal_width 3:sepal_length 4:sepal_width:')
num_feature = int(input())
classification(num_feature)



