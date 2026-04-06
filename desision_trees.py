import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import dtreeviz

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

species_names = ['setosa', 'versicolor', 'virginica']
y_labels = [species_names[label] for label in y]

print("___________________________________________")

# Display class labels
print("Class Labels (Species):")
print(y_labels)

print("___________________________________________")

# Create DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = y_labels
print(df.head())

print("___________________________________________")

# Display sample data for each class
print("Setosa Data:")
print(df[df['target'] == 'setosa'].head(3))

print("\nVersicolor Data:")
print(df[df['target'] == 'versicolor'].head(3))

print("\nVirginica Data:")
print(df[df['target'] == 'virginica'].head(3))

print("___________________________________________")

# Binary Classification: Virginica vs Versicolor
y_binary = (y == 2).astype(int)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y_binary, test_size=0.3, random_state=42
)

# Train Decision Tree
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("___________________________________________")

# Visualization
viz = dtreeviz.model(
    clf,
    X_train,
    y_train,
    target_name='target',
    feature_names=data.feature_names,
    class_names=['versicolor', 'virginica']
)

viz.view()
