
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Create dataset
data = {
    'StudyHours': [1,2,2.5,3,4,5,6,7,8,9],
    'Result': [0,0,0,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)

# 2. Separate X and y
X = df[['StudyHours']]
y = df['Result']

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Create model
model = LogisticRegression()

# 5. Train model
model.fit(X_train, y_train)

# 6. Predict
y_pred = model.predict(X_test)

# 7. Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("Predictions:", y_pred)
print("Actual:", list(y_test))
print("Accuracy:", accuracy * 100, "%")

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# 8. Predict for a new student
new_student = pd.DataFrame([[6]], columns=['StudyHours'])
result = model.predict(new_student)

if result[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")
