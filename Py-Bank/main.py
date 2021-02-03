#import the os module
import os

#import the module for reading the CSV file
import csv

csvpath = os.path.join('..', 'Py-Bank','Resources', 'budget_data.csv')

#lists to store data
month = []
Profit_Loss = []

#Method 2: Improved Reading of CSV Module

with open(csvpath, newline='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    csv_header = next(csvreader)
    for row in csvreader:
     #to check that it's working
        #print (row)

        #Add month
        month.append(row[0])

        #Add Profit/Losses
        Profit_Loss.append(row[1])

        
    