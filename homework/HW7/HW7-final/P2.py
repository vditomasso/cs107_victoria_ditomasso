#!/bin/usr/env python3

import sqlite3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("PRAGMA foreign_keys=1")

cursor.execute('''CREATE TABLE model_params (
                id INTEGER NOT NULL,
                desc TEXT,
                param_name TEXT,
                value REAL)''')

db.commit()

cursor.execute('''CREATE TABLE model_coefs (
                id INTEGER NOT NULL,
                desc TEXT,
                feature_name TEXT,
                value REAL)''')

db.commit()

cursor.execute('''CREATE TABLE model_results (
                id INTEGER NOT NULL,
                desc TEXT,
                train_score,
                test_score)''')
                
db.commit()

# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
    '''Computes test_score and train_score, saves data to the database
    
    Inputs:
    ---
    model_id: Identifier number for the model to save data from
    model_desc: Description of the model to save data from
    db: Database to save data to
    model: A fitted model to save data from
    X_train, X_test, y_train, y_test: Training and test data
    
    Returns:
    ---
    db with the follow enitries added:
    - model_params table, with values from get_params method
    - model_coefs table, with coefficients and intercept values of the fitted model
    - model_results: train and validation accuracy obtained from the score method'''
    
    regr = LogisticRegression()
    regr.fit(X_train, y_train)
    
    params = regr.get_params() # dict, len 15
    coef = regr.coef_ # array (len 1) of array (len 30)
    intercept = regr.intercept_ # array (len 1) containing a float
    train_score = regr.score(X_train, y_train) # float
    test_score = regr.score(X_test, y_test) # float
