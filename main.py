#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pharmahacks - Phyla Challenge #2"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('challenge_1_gut_microbiome_data.csv', index_col=0)

X = df.filter(regex=("Bacteria-*"))
Y = df['disease']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=0)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)

confusion_matrix = pd.crosstab(Y_test, Y_pred, rownames=[
                               'Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)

print('Accuracy - F1 Score - Micro: ', metrics.accuracy_score(Y_test, Y_pred))
print('F1 Score - Macro: ', metrics.f1_score(Y_test, Y_pred, average='macro'))
print('F1 Score - Weighted: ', metrics.f1_score(Y_test, Y_pred, average='weighted'))
#plt.savefig(fname="metrics.png", dpi=300, bbox_inches="tight")


# Actual disease
print(Y_test)
# Prediction
print(Y_pred)
Y_proba = clf.predict_proba(X_test)
# Probability
print(Y_proba)
