# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:00:08 2022

@author: andre
"""

#a script to concatenate all predictions, and create a master document of predictions
import pandas as pd

gold = r'C:\Users\andre\Downloads\fra.tsv'
er = r'C:\Users\andre\Downloads\conjser.tsv'
ir = r'C:\Users\andre\Downloads\conjsir.tsv'
re = r'C:\Users\andre\Downloads\conjsre.tsv'

df_er = pd.read_csv(er, sep='\t', encoding='utf-8')
df_ir = pd.read_csv(ir, sep='\t', encoding='utf-8')
df_re = pd.read_csv(re, sep='\t', encoding='utf-8')
df_gold = pd.read_csv(gold, sep='\t', encoding='utf-8')

frames = [df_er, df_ir, df_re]
df_all_forms = pd.concat(frames)
df_all_forms.to_csv('all_forms.tsv', index=False, encoding='utf-8')