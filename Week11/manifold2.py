from sklearn.datasets import load_digits
from sklearn.manifold import LocallyLinearEmbedding
import matplotlib.pyplot as plt

digits = load_digits()


model = LocallyLinearEmbedding(n_neighbors=50, n_components=2, method='modified',
                               eigen_solver='dense')

out = model.fit_transform(digits.data)

plt.scatter(out[:, 0], out[:, 1],
            c=digits.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('Spectral', 10))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar()
plt.show()