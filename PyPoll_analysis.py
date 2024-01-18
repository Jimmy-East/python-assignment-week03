#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Modules
import os
import csv

# Set path for file
csv_path = os.path.join('Starter_Code', 'PyPoll', 'Resources', 'election_data.csv')

# Output file path
output_path = os.path.join('election_results.txt')

# Initialize variables
votes_total = 0 
candidate_votes = {}

with open(csv_path) as csv_file:
    
    # Read file
    csv_election_data = csv.reader(csv_file, delimiter=',')

    # Skip the header row
    next(csv_election_data)
    
    # Loop through the CSV file contents
    for row in csv_election_data:
        votes_total += 1
        candidate_name = row[2]
        candidate_votes[candidate_name] = candidate_votes.get(candidate_name, 0) + 1  # Update the vote count

# Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)
    
# Display the list of candidates who received votes and their vote counts
with open(output_path, 'a') as output_file:
    output_file.write("Election Results\n")
    output_file.write("--------------------------------------\n")
    output_file.write(f'Total Votes: {votes_total}\n')
    print("Election Results")
    print("--------------------------------------")
    print(f'Total Votes: {votes_total}')
    
    # Iterate over candidates and write their results
    for candidate, votes in candidate_votes.items():    
        percentage = (votes / votes_total) * 100
        output_file.write(f"{candidate}: {percentage:.2f}% ({votes} votes)\n")
        print(f"{candidate}: {percentage:.2f}% ({votes} votes)")

    output_file.write("--------------------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("--------------------------------------\n")
    print("--------------------------------------")
    print("Winner:", winner)
    print("--------------------------------------")


# In[ ]:




