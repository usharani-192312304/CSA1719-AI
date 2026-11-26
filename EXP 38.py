
import numpy as np
from sklearn.svm import SVC

# Input training data
X = np.array([[1, 2], [2, 3], [3, 3],
              [6, 7], [7, 8], [8, 8]])

# Binary class labels
y = np.array([0, 0, 0, 1, 1, 1])

# Create SVM model
model = SVC(kernel='linear')

# Train the model
model.fit(X, y)

# Predict new data
new_data = np.array([[2, 2]])
prediction = model.predict(new_data)

print("SVM Binary Classification")
print("Input Data:", new_data[0])
print("Predicted Class:", prediction[0])
