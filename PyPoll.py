import csv
import os

import csv
import string

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Candidate Votes - empty dictionary
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Use the open statement to open the file as a text file.
with open(file_to_load) as election_data:

    # Read the file object with the reader formula
    file_reader = csv.reader(election_data)

    # Read the file object with the reader formula
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        #2. Add to the total vote count:
        total_votes = total_votes + 1
        
        #Print candidate names from each rom:
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #add candidate name to the candidate list
            candidate_options.append(candidate_name)
            
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add votes to the candidate votes
        candidate_votes[candidate_name] += 1

#Save the results to a text file
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)

        # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
                
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
                
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
                
    #Print out the winning candidate, vote count and percentage:
            
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

            