import pandas as pd 
import numpy as np
import sys
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

# Importing dataset
dataset = pd.read_csv('diabetes.csv')

Y_TestN = list()
Y_TestN.append(int(sys.argv[1]))
Y_TestN.append(int(sys.argv[2]))
Y_TestN.append(float(sys.argv[3]))
Y_TestN.append(int(sys.argv[4]))

Y_TestNN = list()
Y_TestNN.append(Y_TestN)

test_temp=[[97,140,23.2,22]]

dataset.head()

dataset.shape

dataset_new = dataset

dataset_new[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]] = dataset_new[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]].replace(0, np.NaN) 

dataset_new["Glucose"].fillna(dataset_new["Glucose"].mean(), inplace = True)
dataset_new["BloodPressure"].fillna(dataset_new["BloodPressure"].mean(), inplace = True)
dataset_new["SkinThickness"].fillna(dataset_new["SkinThickness"].mean(), inplace = True)
dataset_new["Insulin"].fillna(dataset_new["Insulin"].mean(), inplace = True)
dataset_new["BMI"].fillna(dataset_new["BMI"].mean(), inplace = True)


sc = MinMaxScaler(feature_range = (0, 1))
dataset_scaled = sc.fit_transform(dataset_new)
dataset_scaled = pd.DataFrame(dataset_scaled)

Y_TestNN = sc.fit_transform(Y_TestNN)
Y_TestNN = pd.DataFrame(Y_TestNN)

X = dataset_scaled.iloc[:, [1, 4, 5, 7]].values
Y = dataset_scaled.iloc[:, 8].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 42, stratify = dataset_new['Outcome'])

logreg = LogisticRegression(random_state = 42)
logreg.fit(X_train, Y_train)

predictions = logreg.predict(Y_TestNN)

print(int(predictions[0]))


