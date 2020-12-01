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
                value BLOB)''')

db.commit()

cursor.execute('''CREATE TABLE model_coefs (
                id INTEGER NOT NULL,
                desc TEXT,
                feature_name TEXT,
                value BLOB)''')

db.commit()

cursor.execute('''CREATE TABLE model_results (
                id INTEGER NOT NULL,
                desc TEXT,
                train_score REAL,
                test_score REAL)''')
                
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
    
    # get ready to add to the db
    cursor = db.cursor()
    
    # add to model_params table
    for key, value in params.items():
        cursor.execute('''INSERT INTO model_params (id, desc, param_name, value) VALUES (?, ?, ?, ?)''',
                        model_id, model_desc, key, value)

    # add to model_coefs table
    for feature, coef_val in zip(X_train.columns, coef[0])
        cursor.execute('''INSERT INTO model_coefs (id, desc, feature_name, value) VALUES (?, ?, ?, ?)''',
                        model_id, model_desc+' coef', feature, coef_val)
                        
    cursor.execute('''INSERT INTO model_coefs (id, desc, feature_name, value) VALUES (?, ?, ?, ?)''',
                    model_id, model_desc+' intercept', 'intercept(all)', intercept[0])
                    
    # add to model_results
    cursor.execute('''INSERT INTO model_results (id, desc, train_score, test_score) VALUES (?, ?, ?, ?)''',
                    model_id, model_desc, train_score, test_score)
                    
    db.commit()
    
    return(db)
