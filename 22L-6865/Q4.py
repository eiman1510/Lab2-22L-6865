from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
X = np.array(iris.data)  # Features
Y = np.array(iris.target)  # Target variable

# 1. NumPy Calculations
num_features = X.shape[1]

for i in range(num_features):
    feature_data = X[:, i]  # Extract the i-th feature

    mean = np.mean(feature_data)
    median = np.median(feature_data)
    std_dev = np.std(feature_data)
    min_val = np.min(feature_data)
    max_val = np.max(feature_data)

    print(f"Feature {i+1}:")
    print(f"  Mean: {mean:.2f}")
    print(f"  Median: {median:.2f}")
    print(f"  Standard Deviation: {std_dev:.2f}")
    print(f"  Minimum: {min_val:.2f}")
    print(f"  Maximum: {max_val:.2f}")
    print("-" * 20)

# Extract sepal length and sepal width
sepal_data = X[:, :2]  # Sepal length is the first feature (index 0), sepal width is the second (index 1)
print("Sepal Length and Width Data:\n", sepal_data)

# 2. Matplotlib Visualizations

# Scatter plot of sepal length vs sepal width
plt.figure(figsize=(8, 6))  # Adjust figure size for better readability
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap='viridis')  # X[:, 0] is sepal length, X[:, 1] is sepal width
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width")
plt.colorbar(label="Species", ticks=[0, 1, 2])  # Add a colorbar to show species
plt.show()

# Histogram of sepal length
plt.figure(figsize=(8, 6))
plt.hist(X[:, 0], bins=20, color='skyblue', edgecolor='black')  # Adjust bins for better visualization
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.title("Distribution of Sepal Length")
plt.show()

# Line plot of petal length vs petal width
plt.figure(figsize=(8, 6))
plt.plot(X[:, 2], X[:, 3], marker='o', linestyle='-', color='coral')  # X[:, 2] is petal length, X[:, 3] is petal width
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width")
plt.grid(True)  # Add grid for easier reading
plt.show()
