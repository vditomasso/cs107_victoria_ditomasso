#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 14})
from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import LinearRegression as OLS
from Regression import RidgeRegression as RR

dataset = datasets.load_boston()

X_train, X_test, y_train, y_test = train_test_split(dataset['data'],dataset['target'],test_size=0.2,random_state=42)

alphas = np.linspace(10**-2,10,100)
OLS_model = OLS(alphas[0])
RR_model = RR(alphas[0])

# Fit the RR model at all of the different alphas
RR_scores=[]

for alpha_num in alphas:
    RR_model.set_params(alpha=alpha_num)
    RR_model.fit(X_train,y_train)
    RR_scores.append(RR_model.score(X_test, y_test))
    
# Fit the linear model - doesn't change with alpha
OLS_model.fit(X_train,y_train)
OLS_score = OLS_model.score(X_test, y_test)

# Plot
plt.figure(figsize=[6,5])
plt.plot(alphas,RR_scores, label='Ridge Regression')
plt.plot(alphas, [OLS_score]*len(alphas), label='Linear Regression')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$R^2$')
plt.legend()
plt.semilogx()
plt.savefig('P2F.png')

