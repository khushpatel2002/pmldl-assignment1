# code/datasets/download_dataset.py

import pandas as pd
from sklearn.datasets import fetch_openml

# Fetch the Boston Housing dataset from openml
data = fetch_openml(name='boston', version=1, as_frame=True)

# Combine the features and target into a single DataFrame
df = data.data
df['target'] = data.target

# Save the DataFrame as a CSV file in the current directory
dataset_path = '../../data/boston_housing.csv'
df.to_csv(dataset_path, index=False)

print(f"Dataset downloaded and saved as {dataset_path}")
