import sys
import csv
import glob
import pandas as pd
import os
import time
import logging
from fuzzywuzzy import fuzz
#from openpyxl import Workbook
import numpy as np
import itertools


file="degreeaims.csv"


df_raw=pd.read_csv(file,encoding="unicode_escape")
raw= df_raw['Degree Aim'].tolist()

df_groups=pd.read_excel("C:\\Users\\asayeed\\Documents\\DegreeAims.xlsx",sheet_name="Groups")
groups= df_groups['Degree'].tolist()

df=pd.DataFrame(columns=['A', 'B', 'Ratio'])

for item in raw:
	for group in groups:
            if fuzz.token_set_ratio(item, group) > 90:
                df = df.append({'A': item, 'B':group, 'Ratio': fuzz.token_set_ratio(item, group)}, ignore_index=True)
df.to_csv("list.csv")



file_2="list.csv"


df_2=pd.read_csv(file_2,encoding="unicode_escape")
A= df_2['A'].tolist()

B= df_2['B'].tolist()


df=pd.DataFrame(columns=['A', 'B', 'Ratio'])

for item in A:
	for group in B:
            if fuzz.ratio(item, group) > 70:
                df = df.append({'A': item, 'B':group, 'Ratio': fuzz.token_set_ratio(item, group)}, ignore_index=True)
df.to_csv("list_2.csv")





'''
for a, b in itertools.combinations(raw, 2):
    if fuzz.token_set_ratio(a,b)> 90:
        #print("Comparing: ",a)
        #print("with: ", b)
        #print("similarity ratio: ",fuzz.token_set_ratio(a,b))
        #print(a+"-"+b)

        df=df.append({'A':a, 'B':b, 'Ratio':fuzz.token_set_ratio(a,b)},ignore_index=True)
#print(df)
df.to_csv("list.csv",)


'''



