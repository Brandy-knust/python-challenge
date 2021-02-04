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
    Total_profit = []
   
    for row in csvreader:

        #make lists into values
        month.append(str(row[0]))

        Profit.append(int(row[1]))
        #Diff.append(int(row[3]))
        
        
        Total_profit = 0

        #find the total number of months
        print(len(month))
        
        #find the profits to see it will work
        print(f'{Profit}')

        #find to total profit
        Total_profit = Total_Profit + int(row[1])
        print (Total_profit)




