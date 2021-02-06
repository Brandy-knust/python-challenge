#import the os module
import os

#import the module for reading the CSV file
import csv

csvpath = os.path.join('..', 'Py-Bank','Resources', 'budget_data.csv')
csvoutpath = os.path.join('..', 'Py-Bank', 'Analysis','Financial_Analysis.txt')

#Method 2: Improved Reading of CSV Module


with open(csvpath, newline='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    csv_header = next(csvreader)
   
    #lists to store data
    month = []
    Profit = []
    Diff = []
    First = True
    for row in csvreader:

        #make lists into values
        month.append(str(row[0]))

        Profit.append(int(row[1]))

        #Michael Thomas helped me think of the Diff.append
       
        if not First == True:  
            Diff.append(Profit[-1] - Profit[-2])
        else: 
            First = False


    results = (
    f'Financial Analysis \n'
    f'---------------------------------- \n'
    f'Total Months: {len(month)} \n'
    f'Total: {sum(Profit)} \n'
    f'Average Change: {sum(Diff)/len(month):.2f} \n'
    f'Greatest Increase in Profits: {month[Diff.index(max(Diff))]} {max(Diff)} \n'
    f'Greatest Decrease in Profits: {month[Diff.index(min(Diff))]} {min(Diff)} \n'
    )


    print(results)

    with open (csvoutpath, "w") as text:
        text.write(results)

    #print financial analysis
    
    # print(f'Financial Analysis')
    # print(f'----------------------------------')
    # print(f'Total Months: {len(month)}')
    # print(f'Total: {sum(Profit)}')
    # print(f'Average Change: {sum(Diff)/len(month):.2f}')
    # print(f'Greatest Increase in Profits: {month[Diff.index(max(Diff))]} {max(Diff)}')
    # print(f'Greatest Decrease in Profits: {month[Diff.index(min(Diff))]} {min(Diff)}')
    

# with open (csvoutpath, "w") as text:
#     text.write(f'Financial Analysis\n')
#     text.write(f'----------------------------------\n')
#     text.write(f'Total Months: {len(month)}\n')
#     text.write(f'Total: {sum(Profit)}\n')
#     text.write(f'Average Change: {sum(Diff)/len(month):.2f}\n')
#     text.write(f'Greatest Increase in Profits: {month[Diff.index(max(Diff))]} {max(Diff)}\n')
#     text.write(f'Greatest Decrease in Profits: {month[Diff.index(min(Diff))]} {min(Diff)}\n')

    