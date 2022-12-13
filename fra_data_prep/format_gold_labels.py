# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:39:32 2022

@author: andre
"""
#prep gold labels for comparison with predictions
import pandas as pd

gold = r'C:\Users\andre\Downloads\fra.tsv'
df_gold = pd.read_csv(gold, sep='\t', encoding='utf-8')
del df_gold[df_gold.columns[0]]
df_gold.to_csv('gold.tsv', index=False, encoding='utf-8')