import csv
import pandas as pd


with open('calles_de_medellin_con_acoso.csv', mode ='r')as file:
   
  csvFile = csv.reader(file)
 
  for lines in csvFile:
        print(lines)
        
        
df = pd.read_csv ('calles_de_medellin_con_acoso.csv')
print(df)