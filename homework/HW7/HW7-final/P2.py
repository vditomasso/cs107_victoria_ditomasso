#!/bin/usr/env python3

import sqlite3

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
