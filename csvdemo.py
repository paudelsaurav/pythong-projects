import csv

with open("Data.csv",'r') as file:
    csvread=csv.reader(file)
    for row in csvread:
        print(row)
        
    