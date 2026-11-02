
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV

# 1. Create dataset
data = {
    'StudyHours': [1,2,2.5,3,4,5,6,7,8,9],
    'Attendance': [30,40,45,50,60,65,75,80,90,95],
    'Result': [0,0,0,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)

# 2. Separate X and y
X = df[['StudyHours', 'Attendance']]
y = df['Result']

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Feature scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Create SVM model
model = SVC(kernel='linear', C=1)

# 6. Train model
model.fit(X_train_scaled, y_train)

# 7. Predict
y_pred = model.predict(X_test_scaled)

# 8. Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred) * 100, "%")

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# 9. Predict a new student
new_student = pd.DataFrame([[6, 75]],
                           columns=['StudyHours', 'Attendance'])

new_student_scaled = scaler.transform(new_student)

print("Prediction:", model.predict(new_student_scaled))

# 10. Hyperparameter tuning using GridSearchCV
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

grid = GridSearchCV(
    SVC(),
    param_grid,
    cv=3,
    scoring='accuracy'
)

grid.fit(X_train_scaled, y_train)

print("Best Parameters:", grid.best_params_)

best_model = grid.best_estimator_

y_pred = best_model.predict(X_test_scaled)

print("Tuned Accuracy:",
      accuracy_score(y_test, y_pred))