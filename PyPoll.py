# Retreive the data
import csv
import os
file_to_load= os.path.join("Resources","election_results.csv")
file_to_save=os.path.join("analysis","election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    header=next(file_reader)
    print(header)        
# 1.Get the total number of votes cast
# 2.Get the complete list of candidates who received votes
# 3.Total number of votes each candidate received
# 4.% of win by which the candidate won
# 5.winner based on votes cast