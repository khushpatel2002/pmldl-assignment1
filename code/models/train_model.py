# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from joblib import dump, load

# Set matplotlib style
plt.style.use('seaborn-whitegrid')

# Load Boston dataset
boston = fetch_openml(name='boston', version=1, as_frame=True)

# Initialize the dataframe
data = pd.DataFrame(boston.data)
data.columns = boston.feature_names

# Adding target variable to dataframe
data['PRICE'] = boston.target

# Split features and target variable
X = data.drop(['PRICE'], axis=1)
y = data['PRICE']

# Get the list of feature names
feature_list = X.columns.tolist()

# Calculate the correlation matrix
corr = data.corr()

# Function to extract features with correlation above a certain threshold
def highly_correlated(data, threshold):
    feature = []
    values = []
    for ele, index in enumerate(data.index):
        if abs(data[index]) > threshold:
            feature.append(index)
            values.append(data[index])
    df = pd.DataFrame(data=values, index=feature, columns=["Correlation"])
    return df

# Select features with highest correlation with target variable 'PRICE'
threshold = 0.5
corr_df = highly_correlated(corr['PRICE'], threshold)
print(corr_df)

# Select only highly correlated features
X = X[['RM', 'PTRATIO', 'LSTAT']]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
lm = LinearRegression()
lm.fit(X_train, y_train)

# Convert coefficient values to a dataframe
coefficients = pd.DataFrame([X_train.columns, lm.coef_]).T
coefficients.columns = ['Attribute', 'Coefficients']
print(coefficients)

# Predict on training data
y_pred = lm.predict(X_train)

# Calculate and print evaluation metrics
print('R^2:', metrics.r2_score(y_train, y_pred))
print('Adjusted R^2:', 1 - (1 - metrics.r2_score(y_train, y_pred)) * (len(y_train) - 1) / (len(y_train) - X_train.shape[1] - 1))
print('MAE:', metrics.mean_absolute_error(y_train, y_pred))
print('MSE:', metrics.mean_squared_error(y_train, y_pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_train, y_pred)))

# Save the model using joblib
dump(lm, '../../models/boston_housing_model.joblib')
