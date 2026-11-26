
import numpy as np
from sklearn.cluster import KMeans

# Input dataset
X = np.array([
    [1, 2], [2, 3], [3, 2],
    [8, 8], [9, 8], [8, 9]
])

# Create K-Means model
model = KMeans(n_clusters=2, random_state=42, n_init=10)

# Train the model
model.fit(X)

# Get cluster labels
labels = model.labels_

# Display results
print("K-Means Clustering")
print("Cluster Labels:", labels)
print("Cluster Centers:")
print(model.cluster_centers_)
