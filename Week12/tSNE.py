import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.preprocessing import MinMaxScaler

data = pd.read_excel("data.xlsx")
print(data.head())

MR_data = data.iloc[:, 10:]
print(MR_data.head())

# exclude outlier, scaling


scaler = MinMaxScaler()
MR_scaled = scaler.fit_transform(MR_data)
print(MR_scaled)



kmeans = KMeans(n_clusters=5, random_state=0)
clusters = kmeans.fit_predict(MR_scaled)
print(clusters)


list_SS = []
for i in range(2, 10):
    clusterer = KMeans(n_clusters=i, random_state=10)
    cluster_labels = clusterer.fit_predict(MR_scaled)
    silhouette_avg = silhouette_score(MR_scaled, cluster_labels)
    list_SS.append(silhouette_avg)
print(list_SS)


xx = np.arange(2, 10)
plt.plot(xx, list_SS)
plt.show()


clusters_pd = pd.DataFrame
print(clusters_pd.value_counts)

print(MR_data.pivot_table('CSFVOL', index=clusters, columns=data['CDRGLOB'], aggfunc="count"))



# Project the data: this step will take several seconds
tsne = TSNE(n_components=2, init='random', random_state=0)
data_tsne = tsne.fit_transform(MR_scaled)
print(data_tsne)

list_SS = []
for i in range(2, 10):
    clusterer = KMeans(n_clusters=i, random_state=10)
    cluster_labels = clusterer.fit_predict(data_tsne)
    silhouette_avg = silhouette_score(data_tsne, cluster_labels)
    list_SS.append(silhouette_avg)
print(list_SS)

plt.plot(xx, list_SS)
plt.show()

kmeans = KMeans(n_clusters=6, random_state=0)
clusters = kmeans.fit_predict(data_tsne)
print(clusters)

clusters_pd = pd.DataFrame(clusters)
print(clusters_pd.value_counts)

print(MR_data.pivot_table('CSFVOL', index=clusters, columns=data['CDRGLOB'], aggfunc="count"))


plt.scatter(data_tsne[:, 0], data_tsne[:, 1], c=clusters)
plt.show()
plt.scatter(data_tsne[:, 0], data_tsne[:, 1], c=data["CDRGLOB"])
plt.legend()
plt.show()

