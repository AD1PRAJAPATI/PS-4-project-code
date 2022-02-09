import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('it_salary.csv')
print(df.head(10))

print(df.shape)

print(df.info())
print(df.isnull().sum())
print(df.describe().T)
print(df.level.value_counts())
print(df.company_size.value_counts())
print(df.company_type.value_counts())
print(df[df['salary'] == df.salary.max()])

plt.figure(figsize=(12,6))
sns.boxplot(x=df.level, y=df.salary)

plt.figure(figsize=(12,6))
sns.boxplot(x=df.company_size, y=df.salary)

plt.figure(figsize=(12,6))
sns.boxplot(x=df.company_type, y=df.csalary)

plt.figure(figsize=(10,8))
sns.scatterplot(x = 'yrs_exp', y = 'salary', data = df)

plt.figure(figsize=(10,8))
sns.scatterplot(x = 'yrs_exp', y = 'salary', hue = 'level', data = df)

data = df.copy()

ndata = pd.get_dummies(data, prefix_sep='_')
print(ndata.head())
print(ndata.shape)

print(ndata.info())

ndata = ndata.drop(['level_Junior','company_size_less than 50','company_type_Corporation'], axis='columns')
print(ndata.shape)

print(ndata.head())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, accuracy_score, mean_squared_error

X = ndata.drop('salary',axis=1)

y = ndata.salary
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=50)

lr = LinearRegression()
lr.fit(X_train, y_train)

print("Linear Regression R^2 Score: {:.4f}%".format(lr.score(X_test, y_test)*100))
y_pred = lr.predict(X_test)

print("Linear Regression RMSE: {:.4f}".format(np.sqrt(mean_squared_error(y_test, y_pred))))

diff = y_test - y_pred
print(pd.DataFrame(np.c_[y_test , y_pred , diff] , columns=['Actual','Predicted','Difference']))

print(X_train.iloc[792])
print(y_train.iloc[792])

value = lr.predict([[2,0,1,0,1,0,0,1,0,0]])[0]
print(value)

