#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pharmahacks challenge 1"""

import pandas as pd

features = pd.read_csv('challenge_1_gut_microbiome_data.csv')
print(features.head(5))