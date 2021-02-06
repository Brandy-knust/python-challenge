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
    Khan = []
    Li = []
    Correy = []
    OTooley = []

    #dictionary
    candidate_names = {}
    candidate_names = {"Khan": 0, "Li": 0, "Correy": 0, "O'Tooley": 0}

    Voter_ID = []
    County = []
    Candidate = []

    for row in csvreader:

    #makes lists into values
        Voter_ID.append(str(row[0]))
        County.append(str(row[1]))
        Candidate.append(str(row[2]))

    #find votes by candidate
        for x in candidate_names:
            if isinstance(candidate_names[x], list):
                count += len(candidate_names[x])
    print(count)        


        # Khan.append(int(row[2])) 
        # Li.append(int(row[2]))
        # Correy.append(int(row[2]))
        # OTooley.append(int(row[2]))
        # if [2] is "Khan":
        #     sum(Khan)
            
        # elif [2] is "Li":
        #     sum(Li)
        # elif [2] is "Correy":
        #     sum(Correy)
        
        # else:
        #     sum(OTooley)
               



# #print analysis block
# print (f'Election Results')
# print (f'-----------------------------')
# #print total votes
# print (f'Total Votes {sum(Total_Votes)}')
# print (f'-----------------------------')
# #print percentages votes for each candidate
# print (f'')
# print (f'-----------------------------')
# #print winner
# print (f'')



