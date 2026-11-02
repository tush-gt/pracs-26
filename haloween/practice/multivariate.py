import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# dataset
data = {
    'Area': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400],
    "Bedrooms": [3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
    "Age":[3, 5, 2, 1, 5, 7, 3, 2, 1, 2],
    "Price": [300000, 320000, 340000, 360000, 380000, 400000, 420000, 440000, 460000, 480000]
}

df = pd.DataFrame(data)

# features and target
x = df[['Area','Bedrooms','Age']]
y = df['Price']

# train-test-split
X_train, X_test, Y_train, Y_test= train_test_split(x, y, test_size=0.3, random_state=42)

# model
model = LinearRegression()
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)

# evaluation
mae=mean_absolute_error(Y_test, y_pred)
mse=mean_squared_error(Y_test, y_pred)
r2 = r2_score(Y_test, y_pred)

print("Predicted: ", y_pred)
print("Actual:", list(Y_test))

print("MAE:", mae)
print("MSE:", mse)
print("R2:", r2)

# new values
new_data = pd.DataFrame([[2500, 4, 3]], columns=['Area', 'Bedrooms','Age'])
print("Predicted price for 2500 sq ft, 4 bedrooms, 5 years old house:", model.predict(new_data)[0])