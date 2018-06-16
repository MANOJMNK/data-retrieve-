import pandas as pd
data=pd.read_csv("E:/python//salary.csv")
print(data)

x=data.iloc[:,0:1].values
y=data.iloc[:,1:].values
#dividing and testing data
from sklearn.cross_validation import train_test_split
train_test_split(x,y,train_size=1/7)
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x,y)
y_predict=lr.predict(x)
import matplotlib.pyplot as plt
plt.scatter(x,y,color="r")
plt.plot(x,y_predict)
print(lr.predict(40))
plt.show()