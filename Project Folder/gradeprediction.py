import pandas as pd
import numpy as np
import math

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

import pickle

df = pd.read_csv(r"D:\student_grade_prediction_system\student-mat.csv")

#Remove unnecessary column
df = df.drop(columns=["school", "address", "famsize"])

#convert all text to numbers
df = pd.get_dummies(df, drop_first=True)

#Feature selection
features = ["G1", "G2", "studytime", "absences"]

X = df[features]
y = df["G3"]

#Train - Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Feature scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Train model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#Evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = math.sqrt(mean_squared_error(y_test, y_pred))

#Save the model
import pickle

model_path = r"D:\student_grade_prediction_system\Model\model.pkl"
scaler_path = r"D:\student_grade_prediction_system\Model\Modelscaler.pkl"

with open(model_path, "wb") as f:
    pickle.dump(model, f)

with open(scaler_path, "wb") as f:
    pickle.dump(scaler, f)

# IMPORT LIBRARIES

import pickle
import numpy as np
import pandas as pd

# LOAD MODEL

with open(r"D:\student_grade_prediction_system\Model\model.pkl", "rb") as f:
    model = pickle.load(f)

with open(r"D:\student_grade_prediction_system\Model\Modelscaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# USER INTERFACE

print("\n Student Grade Prediction System")
print("--------------------------------------------------")
print("Enter values within the following ranges:\n")

print("G1 (First Grade): 0 - 20")
print("G2 (Second Grade): 0 - 20")
print("Study Time: 1 - 4 (1=low, 4=high)")
print("Absences: 0 - 100\n")


# INPUT VALIDATION

while True:
    try:
        G1 = float(input("Enter G1 (0-20): "))
        G2 = float(input("Enter G2 (0-20): "))
        studytime = float(input("Enter Study Time (1-4): "))
        absences = float(input("Enter Absences (0-100): "))

        if not (0 <= G1 <= 20):
            print("G1 must be between 0 and 20")
            continue
        if not (0 <= G2 <= 20):
            print("G2 must be between 0 and 20")
            continue
        if not (1 <= studytime <= 4):
            print("Study time must be between 1 and 4")
            continue
        if not (0 <= absences <= 100):
            print("Absences must be between 0 and 100")
            continue

        break

    except ValueError:
        print("Please enter valid numeric values")


# PREPARE INPUT

feature_names = ["G1", "G2", "studytime", "absences"]

data = pd.DataFrame([[G1, G2, studytime, absences]], columns=feature_names)

data = scaler.transform(data)


# PREDICT

prediction = model.predict(data)

# Clip result between 0–20
grade = max(0, min(20, prediction[0]))


# OUTPUT

print("\nPredicted Final Grade (G3):", round(grade, 2))

# INTERPRET RESULT

if grade >= 16:
    print("Excellent Performance")
elif grade >= 12:
    print("Good Performance")
elif grade >= 8:
    print("Average Performance")
else:
    print("Needs Improvement")


