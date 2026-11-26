
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Input dataset
X = np.array([
    [2, 4, 6],
    [3, 5, 7],
    [4, 6, 8],
    [5, 7, 9],
    [6, 8, 10]
])

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_scaled)

# Display results
print("Original Data Shape:", X.shape)
print("Reduced Data Shape:", X_reduced.shape)
print("Reduced Dataset:")
print(X_reduced)
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)
