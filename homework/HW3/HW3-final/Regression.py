#!/usr/bin/env python3

import numpy as np

class Regression():

    def __init__(self, alpha):
        # Initializes an empty dictionary called params
        self.params = {'alpha':alpha}

    def fit(self, X, y):
        # Fits a linear model to X and y. It stores best-fit parameters in the dictionary attribute called params. The first key should be the coefficients (not including the intercept) and the second key should be the intercept.
        raise NotImplementedError

    def predict(self, X):
        # Predict new values with the fitted model given X.
        return(np.dot(X,self.params['coeff']))

    def score(self, X, y):
        # Returns the R2 value of the fitted model.
        SST = np.sum(pow(y-np.mean(y),2))
        y_predict = self.predict(X)
        SSE = np.sum(pow(y-y_predict,2))
        R2 = 1-(SSE/SST)
        return(R2)
        
    def get_params(self):
        # Returns βˆ for the fitted model. Note that the fit method already stored the dictionary in params, so all you need to do is return that dictionary.
        return(self.params)

    def set_params(self, **kwargs):
        # Manually set parameters of the linear model. The method should accept variable keyword arguments (**kwargs) containing model parameters. In this problem, it will be used to set the reguarization coefficient α in the Ridge Regression model.
        self.params.update(kwargs)

class LinearRegression(Regression):

    def fit(self, X, y):
        X_transpose = X.transpose()
        term1 = np.dot(X_transpose,X)
        term1_inv = np.linalg.pinv(term1)
        term2 = np.dot(term1_inv, X_transpose)
        best_fit_coeff = np.dot(term2,y)
        self.params['coeff'] = best_fit_coeff

class RidgeRegression(Regression):

#    def __init__(self,alpha):
#        super().__init__(alpha)

    def fit(self, X, y):
        I = np.identity(X.shape[1])
        gamma = self.params['alpha']*I
        X_transpose = X.transpose()
        gamma_transpose = gamma.transpose()
        X_term = np.dot(X_transpose,X)
        gamma_term = np.dot(gamma_transpose, gamma)
        sum_terms = X_term+gamma_term
        sum_terms_inv = np.linalg.inv(sum_terms)
        term1 = np.dot(sum_terms,X_transpose)
        best_fit_coeff = np.dot(term1,y)
        self.params['coeff'] = best_fit_coeff

from sklearn.datasets import load_boston
X, y = load_boston(return_X_y=True)

#test_reg = Regression()
#test_reg.fit(X,y)

test_lin=RidgeRegression(0.1)
test_lin.fit(X,y)
print(test_lin.get_params())
print(test_lin.score(X,y))

# Here are the working regression functions, not implemented into the class
# FOR THIS CLASS AND THE RIDGEREGRESSION CLASS, INSTEAD OF HAVING AN INTERNAL FUNCTION WITH INPUTS, JUST INITIALIZE USING THE ATTRIBUTES OF THE CLASS

#def OLSfit(X,y):
#    '''Input:
#    X: matrix, size n x p
#    y: vector, len n
#    Returns:
#    best_fit_coeff: vector, len p'''
#    # best_fit_coeff = (X_transpose X)^-1 X_transpose y
#    X_transpose = X.transpose()
#    term1 = np.dot(X_transpose,X) # I might want these dots to be matmuls
#    term1_inv = np.linalg.inv(term1)
#    term2 = np.dot(term1_inv, X_transpose)
#    best_fit_coeff = np.dot(term2,y)
#    return(best_fit_coeff)
#
#def RRfit(X,y, alpha):
#    I = np.identity(X.shape[1])
#    gamma = alpha*I
#    X_transpose = X.transpose()
#    gamma_transpose = gamma.transpose()
#    X_term = np.dot(X_transpose,X)
#    gamma_term = np.dot(gamma_transpose, gamma)
#    sum_terms = X_term+gamma_term
#    sum_terms_inv = np.linalg.inv(sum_terms)
#    term1 = np.dot(sum_terms,X_transpose)
#    best_fit_coeff = np.dot(term1,y)
#    return(best_fit_coeff)
