#import the os module
import os

#import the module for reading the CSV file
import csv

csvpath = os.path.join('..', 'Py-Poll','Resources', 'election_data.csv')

#Method 2: Improved Reading of CSV Module


with open(csvpath, newline='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
