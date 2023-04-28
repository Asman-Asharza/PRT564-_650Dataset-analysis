import pandas as pd
import numpy as np
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

# Train the k-means model with the optimal number of clusters
kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(X)

# Show the cluster characteristics
for i, center in enumerate(kmeans.cluster_centers_):
    print(f'Cluster {i+1}:\n\nPwnCount: {center[0]:.2f}\nVerified: {center[1]:.2f}\nFabricated: {center[2]:.2f}\nSensitive: {center[3]:.2f}\nRetired: {center[4]:.2f}\nSpamList: {center[5]:.2f}\nMalware: {center[6]:.2f}\n')

