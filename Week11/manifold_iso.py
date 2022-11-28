from sklearn.datasets import load_digits
from sklearn.manifold import Isomap
from matplotlib import offsetbox
import numpy as np
import matplotlib.pyplot as plt

digits = load_digits()


model = Isomap(n_neighbors=50, n_components=2)
proj = model.fit_transform(digits.data)
print(proj.shape)


def plot_components(data, model, images=None, ax=None,
                    thumb_frac=0.05, cmap='gray'):
    ax = ax or plt.gca()

    proj = model.fit_transform(data)
    ax.plot(proj[:, 0], proj[:, 1], '.k')

    if images is not None:
        min_dist_2 = (thumb_frac * max(proj.max(0) - proj.min(0))) ** 2
        shown_images = np.array([2 * proj.max(0)])
        for i in range(data.shape[0]):
            dist = np.sum((proj[i] - shown_images) ** 2, 1)
            if np.min(dist) < min_dist_2:
                # don't show points that are too close
                continue
            shown_images = np.vstack([shown_images, proj[i]])
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(images[i], cmap=cmap),
                proj[i])
            ax.add_artist(imagebox)


fig, ax = plt.subplots(figsize=(10, 10))
plot_components(digits.data,
                model=Isomap(n_components=2),
                images=digits.images[:, ::2, ::2])
