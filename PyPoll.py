
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

#Initialize string for winning candidate
winning_candidate = ''

#Initialize winning count to 0
winning_count = 0

#Winning % initialize to 0
winning_percentage = 0

#Assigning a variable for the file to load and the path
file_to_load = os.path.join('election_results.csv')

#Assigning a variable to save file
file_to_save = os.path.join('election_analysis.txt')

#Open the election results file and read
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#Read the header row
    headers = next(file_reader)
    
#Print each row in the CSV
    for row in file_reader:
        total_votes += 1

        #Skip header row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            #Identify the distinct candidates
            candidate_options.append(candidate_name)
            #Begin tracking votes for each candidate
            candidate_votes[candidate_name] = 0
        #Increment the votes for each candidate
        candidate_votes[candidate_name] += 1
    
    #Find the percentage of votes
    for candidate_name in candidate_votes:
        #Count each vote for the candidates
        votes = candidate_votes[candidate_name]
        #Calculate percentage of votes 
        vote_percentage = float(votes)/float(total_votes) * 100
        

        #Determining the winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f'------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}\n'
    f'------------------\n')

#print(candidate_votes)

### Currently this is only printing one result... need to figure out why only one result is returning
#print(f'{candidate_name}: has {vote_percentage:.1f}% of the vote')

#Print out winning candidate
print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

print(winning_candidate_summary)
     
