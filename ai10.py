import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix

file_path='C:\python\Python37\iris.csv'
iris_data=pd.read_csv(file_path)

X=iris_data.iloc[:,:-1].values
y=iris_data.iloc[:,-1].values

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
naive_bayes=GaussianNB()
naive_bayes.fit(X_train,y_train)
y_pred=naive_bayes.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print("accuracy:",accuracy)
conf_matrix=confusion_matrix(y_test,y_pred)
print("confusion matrix:")
print(conf_matrix)
