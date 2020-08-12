
# The data that needs to be collected

# 1) Total votes cast

# 2) Comprehensive list of candidates that received votes

# 3) Percantage of votes that each candidate won

# 4) Total number of votes each candidate won

# 5) The winning candidate by total popular vote


#Create imports
import os
import csv

#Initialize variable for votes
total_votes = 0

#Candidate options
candidate_options = []

#Dictionary for candidate votes
candidate_votes = {}

#Assigning a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')

#Assigning a variable to save file
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#Open the election results file and read
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#Read the header row
    headers = next(file_reader)
    
#Print each row in the CSV
    for row in file_reader:
        total_votes += 1
        

        #Print the candidate name for each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            #Identify the distinct candidates
            candidate_options.append(candidate_name)
            #Begin tracking votes for each candidate
            candidate_votes[candidate_name] = 0
        #Increment the votes for each candidate
        candidate_votes[candidate_name] += 1
    
    #Find the percantage of votes
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percantage = float(votes)/float(total_votes) * 100
        
### Currently this is only printing one result... need to figure out why only one result is returning
print(f'{candidate_name}: has {vote_percantage:.2f}% of the vote')





