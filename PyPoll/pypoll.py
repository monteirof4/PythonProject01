#Import OS Module
import os
#Import CSV module
import csv

#Direct to CSV path with raw data
csv_path = os.path.join('Resources','election_data.csv')

#Define output file path
output_file = os.path.join('Resources',"election_results.txt")

#open CSV file
with open(csv_path, newline='') as csvfile:
    #make CSV reader
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header
    next(csvreader)
    
    totalvotes = 0 #Variable to store total votes data

    #create lists to store file data
    candidate = []
    candidate_votes = []

    #Read file and store data in lists
    for row in csvreader:
        totalvotes += 1
        if row[2] not in candidate:
            candidate.append(row[2])
            candidate_votes.append(1)
        else:
            candidate_votes[candidate.index(row[2])] += 1
    
vote_percentage = []
    
for item in range(len(candidate_votes)):
    vote_percentage.append(round((candidate_votes[item] / totalvotes)*100,0))

#Sorting the Candidates Votes list
candidate_votes_sort = sorted(candidate_votes, reverse = True)

#Print out results to terminal and write to the outputfile
with open(output_file, 'w') as text:

    print('Election Results')
    text.write('Election Results\n')
    print('-------------------------')
    text.write('-------------------------\n')
    print(f'Total Votes: {totalvotes}')
    text.write(f'Total Votes: {totalvotes}\n')
    print('-------------------------')
    text.write('-------------------------\n')
    #Finding the sorted index to retrieve the correct data
    for x in range(len(candidate)):
        for y in range(len(candidate)):
            if candidate_votes[y] == candidate_votes_sort[x]:
                index = candidate_votes.index(candidate_votes[y])
                print(f"{candidate[index]}: {vote_percentage[index]:6.3f}% ({candidate_votes[index]})")
                text.write(f"{candidate[index]}: {vote_percentage[index]:6.3f}% ({candidate_votes[index]})\n")
    print('-------------------------')
    text.write('-------------------------\n')
    
    #Find the winner
    greatestvote = max(candidate_votes) #Finding Greatest number of votes
    winner = candidate[candidate_votes.index(greatestvote)]
    print(f'Winner: {winner}')
    text.write(f'Winner: {winner}\n')
    print('-------------------------')
    text.write('-------------------------\n')
        
    
    

