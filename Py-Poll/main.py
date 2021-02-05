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

Total_Votes = 0
Candidate_Votes = 1
Name_list = []

Voter_ID = []
County = []
Candidate = []






#print analysis block
print (f'Election Results')
print (f'-----------------------------')
#pring total votes
print (f'Total Votes {sum(Total_Votes)}')
print (f'-----------------------------')
#print percentages votes for each candidate
print (f'')
print (f'-----------------------------')
#print winner
print (f'')
