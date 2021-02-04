#import the os module
import os

#import the module for reading the CSV file
import csv

csvpath = os.path.join('..', 'Py-Bank','Resources', 'budget_data.csv')


#Method 2: Improved Reading of CSV Module


with open(csvpath, newline='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
   
    #lists to store data
    month = []
    Profit = []
    Profit.append(0)
    Diff = []
   
    for row in csvreader:

        #make lists into values
        month.append(str(row[0]))

        Profit.append(int(row[1]))

        #Michael Thomas helped me think of the Diff.append
        Diff.append(Profit[-1] - Profit[-2])

    Profit.pop(0)
    #print financial analysis
    print(f'Financial Analysis')
    print(f'----------------------------------')
    print(f'Total Months: {len(month)}')
    print(f'Total: {sum(Profit)}')
    print(f'Average Change: {sum(Diff)/len(month):.2f}')
    print(f'Greatest Increase in Profits: {month[Diff.index(max(Diff))]} {max(Diff)}')
    print(f'Greatest Decrease in Profits: {month[Diff.index(min(Diff))]} {min(Diff)}')
    


        
    