# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 20:55:52 2022

@author: andre
"""
#sorting the lemmas in fra.tsv according to ending
#these lemmas will be passed to the analyzer, which conducts analysis based on infinitival ending 
import pandas as pd

file_in = r'C:\Users\andre\Downloads\fra.tsv'
er_out = r'verbs_er.tsv'
ir_out = r'verbs_ir.tsv'
re_out = r'verbs_re.tsv'

with open(file_in, encoding='utf-8') as input_, open(er_out, 'w', encoding='utf-8') as er_output, open(ir_out, 'w', encoding='utf-8') as ir_output, open(re_out, 'w', encoding='utf-8') as re_output:
    df = pd.read_csv(input_, sep='\t', encoding='utf-8')
    one = df.iloc[:, [0]]
    no_dupes = one.drop_duplicates()
    onedim = no_dupes.squeeze()
    
    for item in onedim:
        if item.endswith("er"):
            print(item, file = er_output)
        elif item.endswith("ir"):
            print(item, file = ir_output)
        elif item.endswith("re"):
            print(item, file = re_output)