#import the os module
import os

#import the module for reading the CSV file
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

#Method 2: Improved Reading of CSV Module

with open(csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #Read the header row first
    csv_header = next(csvreader)

    print(csv_header{1})
    print(len(csvfile))
    