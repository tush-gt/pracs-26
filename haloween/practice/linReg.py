import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

#create dataset
data = {
    'Experience': [1,2,3,4,5,6,7,8,9,10],
    'Salary': [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
}

df = pd.DataFrame(data)

# features and target
x=df[['Experience']]
y=df['Salary']

# train-test-split
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# model
model = LinearRegression()

# train fit
model.fit(X_train, Y_train)

# pred
y_pred = model.predict(X_test)


# evaluation
print("Predicted: ", y_pred)
print("Actual: ", list(Y_test))

mae = mean_absolute_error(Y_test, y_pred)
mse = mean_squared_error(Y_test, y_pred)
r2 = r2_score(Y_test, y_pred)

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R-squared (R2):", r2)

# unseen value
new_data = pd.DataFrame({'Experience':[11]})
predicted_salary = model.predict(new_data)
print("Predicted salary for 11 years of experience:", predicted_salary[0])































# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats
# from sklearn.metrics import mean_squared_error, mean_absolute_error

# #dataset
# exp = np.array([1,2,3,4,5,6,7,8,9,10])
# sal = np.array([15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

# #Linear regress
# slope, intercept, r_value, p_value, std_err = stats.linregress(exp, sal)

# y_pred = slope*exp + intercept
# #model

# #evaluation
# mse = mean_squared_error(sal, y_pred)
# r2 = r_value ** 2
# mae =mean_absolute_error(sal, y_pred)

# print("Slope: ",slope, "\nIntercept:", intercept, "\nR2=", r2, "\nMSE=", mse, "\nMAE", mae)

# # predict new salary
# new_sal = slope*11 + intercept
# print("Predicted salary for experience 11 years: ", new_sal)


# plt.scatter(exp, sal, color='blue')
# plt.plot(exp, y_pred, color='red')
# xlabel="Experience (years)"
# ylabel="Salary (thousands)"
# plt.show()



# RULES #
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import linregress
# from sklearn.metrics import mean_squared_error, mean_absolute_error
#create dataset dummy
#linear regression
#slope, intercept, r_value, p_value, std_err = linregress(exp,sal)
# y_pred = slope*exp + int
# model done, now evaluation
#mae, mse, r2=r_value**2 - print all
# now graphs
