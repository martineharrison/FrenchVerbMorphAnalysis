# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:50:37 2022

@author: andre
"""
#a script to calculate error for the analyzer's output
import pandas as pd

#open files containing gold labels and hypothesis labels as pandas dataframes
gold = r'fra_gold.tsv'
preds = r'fra_preds.tsv'
df_gold = pd.read_csv(gold, encoding='utf-8')
df_preds = pd.read_csv(preds, encoding = 'utf-8')

#concatenate gold labels and hypothesis labels; remove all labels that are shared between 
#dataframes (so, delete the center of the venn diagram)
frames = [df_gold, df_preds]
all_labels = pd.concat(frames)
error_df = all_labels.drop_duplicates(keep = False)

#merge gold labels with the error dataframe; add all labels which do not also appear in the 
#gold results to an error count, then calculate WER based off of error count
merged_df = pd.merge(error_df, df_gold, how='outer', indicator=True)
errors = 0
for item in merged_df['_merge']:
    if item == 'left_only':
        errors += 1
total = df_gold.shape[0]
#write out evaluative results to a .txt file
with open('fra_results.txt', 'w', encoding='utf-8') as results:
    print('word error rate is: ' + str(round(100 * errors / total)), file = results)