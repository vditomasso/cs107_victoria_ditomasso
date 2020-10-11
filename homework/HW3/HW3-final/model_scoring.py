#!/usr/bin/env python3
from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import LinearRegression as OLS
from Regression import RidgeRegression as RR

dataset = datasets.load_boston()

X_train, X_test, y_train, y_test = train_test_split(dataset['data'],dataset['target'],test_size=0.2,random_state=42)

alpha=0.1
models = [OLS(), RR()]

for model in models:
    model.fit(X_train, y_train, alpha=alpha)
    score = model.score(X_test, y_test)
    best_params = model.get_params()
    print('R2=',score,' params=',best_params)

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
