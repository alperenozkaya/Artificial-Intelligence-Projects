import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
X_iris = iris.drop('species', axis=1)
#print(iris)

#sns.lmplot(x="petal_length", y="petal_width", hue='species', data=iris, fit_reg=False)
#plt.show()

from sklearn.decomposition import PCA  # 1. Choose the model class
model = PCA(n_components=2)            # 2. Instantiate the model with hyperparameters
model.fit(X_iris)                      # 3. Fit to data. Notice y is not specified!
X_2D = model.transform(X_iris)

iris['PCA1'] = X_2D[:, 0]
iris['PCA2'] = X_2D[:, 1]
#sns.lmplot(x="PCA1", y="PCA2", hue='species', data=iris, fit_reg=False)
#plt.show()

#print(model.components_)
#print(iris['PCA1'])
import pandas as pd
pd.options.display.max_rows = 999
#print(iris)

from sklearn import mixture
model = mixture.GaussianMixture(n_components=6,
            covariance_type='full')  # 2. Instantiate the model with hyperparameters
model.fit(X_iris)                    # 3. Fit to data. Notice y is not specified!
y_gmm = model.predict(X_iris)
iris['cluster'] = y_gmm
sns.lmplot(x="PCA1", y="PCA2", data=iris, hue='species',
           col='cluster', fit_reg=False)
plt.show()

