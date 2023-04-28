import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv('/Users/solin/IdeaProjects/databreach/databreaches650.csv')

# Select the features to be used for clustering
features = ['PwnCount', 'IsVerified', 'IsFabricated', 'IsSensitive', 'IsRetired', 'IsSpamList', 'IsMalware']
X = data[features].values

# Determine the optimal number of clusters using the elbow method
distortions = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    distortions.append(kmeans.inertia_)
plt.plot(range(1, 11), distortions)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()

# Train the k-means model with the optimal number of clusters
kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(X)

# Visualize the clusters
plt.scatter(X[pred_y == 0, 0], X[pred_y == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X[pred_y == 1, 0], X[pred_y == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X[pred_y == 2, 0], X[pred_y == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(X[pred_y == 3, 0], X[pred_y == 3, 1], s=100, c='cyan', label='Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('PwnCount')
plt.ylabel('Sensitive')
plt.legend()
plt.show()
