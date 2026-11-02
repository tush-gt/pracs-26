
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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

# 4. BAGGING - Random Forest
bagging_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

bagging_model.fit(X_train, y_train)

bagging_pred = bagging_model.predict(X_test)

# 5. BOOSTING - AdaBoost
boosting_model = AdaBoostClassifier(
    n_estimators=50,
    random_state=42
)

boosting_model.fit(X_train, y_train)

boosting_pred = boosting_model.predict(X_test)

# 6. Compare accuracy
print("Bagging Accuracy:",
      accuracy_score(y_test, bagging_pred) * 100)

print("Boosting Accuracy:",
      accuracy_score(y_test, boosting_pred) * 100)

# 7. Confusion matrices
print("Bagging Confusion Matrix:")
print(confusion_matrix(y_test, bagging_pred))

print("Boosting Confusion Matrix:")
print(confusion_matrix(y_test, boosting_pred))

# 8. Classification reports
print("Bagging Report:")
print(classification_report(y_test, bagging_pred, zero_division=0))

print("Boosting Report:")
print(classification_report(y_test, boosting_pred, zero_division=0))
