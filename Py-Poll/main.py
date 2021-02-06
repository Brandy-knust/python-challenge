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

#lists to sort and store

Total_Votes = 0
Candidate_Votes = 1
Name_list = []

#dictionary
candidate_names = {}
candidate_names = dict()

Voter_ID = []
County = []
Candidate = []

for row in csvreader:

    #makes lists into values
    Voter_ID.append(str(row[0]))
    County.append(str(row[1]))
    Candidate.append(str(row[2]))

    #find votes by candidate
    



# #print analysis block
# print (f'Election Results')
# print (f'-----------------------------')
# #pring total votes
# print (f'Total Votes {sum(Total_Votes)}')
# print (f'-----------------------------')
# #print percentages votes for each candidate
# print (f'')
# print (f'-----------------------------')
# #print winner
# print (f'')

print (f'{candidate_names}')

