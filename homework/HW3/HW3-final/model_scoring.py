#!/usr/bin/env python3
from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import LinearRegression as OLS
from Regression import RidgeRegression as RR

dataset = datasets.load_boston()

X_train, X_test, y_train, y_test = train_test_split(dataset['data'],dataset['target'],test_size=0.2,random_state=42)

alpha=0.1
models = [OLS(alpha), RR(alpha)]

scores=[]
params = []

for model in models:
    model.fit(X_train, y_train)
    scores.append(model.score(X_test, y_test))
    params.append(model.get_params())

print('Linear Regression R2=',scores[0],' Ridge Regression R2=',scores[1])

if scores[0]<scores[1]:
    print('Best params (linear) =',params[0])
else:
    print('Best params (ridge) =',params[1])

#from sklearn import datasets
#from sklearn.model_selection import train_test_split
##import regression classes
#
#dataset = datasets.load_diabetes()
#X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
#                                                    dataset['target'],
#                                                    test_size=0.2,
#                                                    random_state=42)
#
#alpha = 0.5
#models = [model1(alpha), model2(alpha)]
#
#for model in models:
#    model.fit(X_train, y_train);
