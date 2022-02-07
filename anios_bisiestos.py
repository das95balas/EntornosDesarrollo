# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 10:55:38 2021

@author: DavidAlcázarSánchez
"""

year = 1999
listayears = []

for year in range (1999,2101):
    if year % 4 == 0:
        listayears += [year]
    year = year + 1
   
for year in listayears:
    if year % 100 != 0 or year % 400 == 0:
        print (f"El {year} fue o será un año bisiesto.")








