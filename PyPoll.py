# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load= os.path.join("election-analysis","Resources","election_results.csv")
# Assign a variable to save a file from a path.
file_to_save=os.path.join("election-analysis","analysis","election_analysis.txt")

#initiate total votes
total_votes=0

# Print the candidate name from each row
candidate_options=[]

# creating empty dictionary for candidate votes
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # read the header row   
    header=next(file_reader)
    print(header)    
    
    # print each row in the CSV file
    for row in file_reader:
            
        # 1.Get the total number of votes cast
        total_votes +=1 
        
        # name of every candidate
        candidate_name=row[2]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

         # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    

# Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
     winning_count = votes
     winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
     winning_candidate = candidate_name
     
# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


