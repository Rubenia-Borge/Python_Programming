# -*- coding: utf-8 -*-
"""Day26.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x1rHSoG_YxCqYgfiiWabs80iNFefKOfN

100 Days of Code,
Day 26,
Rubenia Borge
"""

import pandas as pd
import numpy as np
companySales = {'Sex':['Children','Children','Children','Men','Men','Men', 'Men','Women','Women', 'Women', 'Women'], 
                'Class' : ['First','Second','Third','First','Second','Third','Crew', 'First', 'Second', 'Third','Crew'], 
                'Survived': [6,24,27,57,14,75,192,140,80,76,20], 
                'Died':[0,0,52,118,154,387,693,4,13,89,3]}
df = pd.DataFrame(companySales,columns=["Sex","Class","Survived","Died"])
print(df)

new_df = df[(df['Class'] == 'First')]
print(new_df)

df.index = ['First','Second','Third','First','Second','Third','Crew', 'First', 'Second', 'Third','Crew']
print(df.drop(["Crew"]))

df['Number'] = (df['Survived'] + df['Died'])
print(df)

df['Percentage'] = (df['Survived']/df['Number'])*100
print(df)

df.drop(["Number"], axis = 1)

new_df = df[(df['Percentage'] > 80)]
print(new_df)

new_df = df[(df['Percentage'] < 40)]
print(new_df)

grouped = df.groupby('Class')
print("Survived", grouped['Survived'].sum()) 
print()
print("Died", grouped['Died'].sum())

df.to_csv('titanic_data.csv',encoding='utf-8', index=False)

df.to_csv('titanic_data2.csv',encoding='utf-8', index=False)

titanic2 = pd.read_csv('titanic_data2.csv')
print(titanic2)

df = pd.read_csv('heart.txt', sep=' ' ,names = ['age','sex','chest_pain','bp','chol','sugar','ecg','heart_rate','angina','oldpeak','slope','vessel','thal','disease'] )
print(df)

df["age"]

print("Mean")
print(df['age'].mean())
print()
print("Standard Deviation")
print(df['age'].std())

print("Younger than 55")
young_df = df[(df['age'] < 55) ]
print(young_df)
print(" ")
print("Older than 55")
old_df = df[(df['age'] > 55) ]
print(old_df)

grouped = df.groupby('disease')
print (grouped['age'].mean(), grouped['bp'].mean(), grouped['chol'].mean(),grouped['heart_rate'].max())