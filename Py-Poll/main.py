#import the os module
import os

#import the module for reading the CSV file
import csv

csvpath = os.path.join('..', 'Py-Poll','Resources', 'election_data.csv')
csvoutpath = os.path.join('..', 'Py-Poll', 'Analysis', 'election_results.txt')

#Method 2: Improved Reading of CSV Module


with open(csvpath, newline='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    

    csv_header = next(csvreader)

    #lists to sort and store

    Total_Votes = 0
    # Candidate_Votes = 1
    Name_list = []
    # Khan = []
    # Li = []
    # Correy = []
    # OTooley = []

    #dictionary
    candidate_dict = {}
    #candidate_names = {"Khan": 0, "Li": 0, "Correy": 0, "O'Tooley": 0}

    # Voter_ID = []
    # County = []
    # Candidate = []
    Count = 0
    print(f'Election Results \n')
    print(f'-----------------------------\n')
    for row in csvreader:

        Total_Votes += 1
        candidate_names = row[2]
        if candidate_names not in Name_list:
            Name_list.append(candidate_names)
            candidate_dict[candidate_names]=0
        candidate_dict[candidate_names]  += 1
  
    print(f'Total_Votes = {Total_Votes}\n')
    print(f'-----------------------------\n')
    max = 0
    Winner = ""
    for i, (key, value) in enumerate(candidate_dict.items()):

 
        percentage_vote = value / Total_Votes *100
        print (f'{key} - {round(percentage_vote,2)} % - ({value})\n')
        
        if value > max:
            max = value 
            winner = key
    print (f'-----------------------------')        
    print (f'{winner} is the winner')



with open (csvoutpath, "w") as text:
    text.write(f'Election Results \n')
    text.write(f'-----------------------------\n')
    text.write(f'Total_Votes = {Total_Votes}\n')
    text.write(f'-----------------------------\n')
    text.write(f'{key} - {round(percentage_vote,2)} % - ({value})\n')
    text.write(f'-----------------------------\n')
    text.write(f'{winner} is the winner')



# # #print analysis block
# # print (f'Election Results')
# # print (f'-----------------------------')
# print Total Votes
# print (f'Total_votes')
# # print (f'-----------------------------')
# # #print percentages votes for each candidate
# # print (f'')
# # print (f'-----------------------------')
# # #print winner
# # print (f'')



