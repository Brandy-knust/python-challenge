#import the os module
import os

#import the module for reading the CSV file
import csv

csvpath = os.path.join('..', 'Py-Bank','Resources', 'budget_data.csv')



#set counter
# month_counter = 0
# Profit = 0
# difference_profit = 0
# Average_prof = 0

#Method 2: Improved Reading of CSV Module


with open(csvpath, newline='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
   
    #lists to store data
    month = []
    Profit = []
   
    for row in csvreader:

        month.append(str(row[0]))

        Profit.append(int(row[1]))
        #Diff.append(int(row[3]))
    print(len(month))

    print(f'{Profit}')

