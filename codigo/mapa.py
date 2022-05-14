import csv
import pandas as pd
import numpy as np
import networkx as nx
from sympy import source

with open('calles_de_medellin_con_acoso.csv', mode ='r')as file:
   
  csvFile = csv.reader(file)
  
  
df = pd.read_csv ('calles_de_medellin_con_acoso.csv', sep=';',index_col=None)
M = nx.from_pandas_edgelist(df,source='origin',target='destination',edge_attr='length')
M.nodes()
M.edges()
M.order()
for x in M.nodes():
      if M.degree(x) > 2:
            print(x) 
djk_path=nx.dijkstra_path(M,source='(-75.5728593, 6.2115169)',target='(-75.5840831, 6.3071118)')
djk_path
