 A Python Analysis of Election Results

## Overview & Purpose
The analyst was tasked with assisting Tom, a Colorado board of elections employee, in an election audit of tabulated results for a U.S. congressional precinct in Colorado.  Tom's manager wanted to automate the audit process with Python and create a script that could report the total number of votes cast, total number of votes for each candidate, total number of votes in each county, percentage of votes for each candidate, percentage of votes from each county, winner of the election based on the popular vote, and the county with the highest voter turnout. With this script, Tom and his team can analyze not only this election, but any election, and get a reliable result just by modifying a few lines of code.

## Election Audit Process and Results
The script read through the election_results.csv file to create an analysis to determine different metrics of voter data between candidates and counties, and generate a txt file giving the result.  An explanation of the methods of analysis and results are bulleted below:

- Total vote count:
    
    - There were *369,711* total votes cast in the election (see .txt output below):

        [Total_Votes.png](https://github.com/hillmanj1995/Election_Analysis/blob/main/Resources/Total_Votes.png)
    - The following excerpts of code were used to determine that value ("..." signifies portions of code that do not directly apply to the method in question):
        
            '#Initialize a total vote counter.
            total_votes = 0

            ...

            #For each row in the CSV file.
            for row in reader:

                # Add to the total vote count
                total_votes = total_votes + 1
        
            ...

            # Print the final vote count (to terminal)
            election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------\n\n"
                f"County Votes:\n")
            print(election_results, end="")

            txt_file.write(election_results)

- Vote count and percentage of votes per county:
    
    - The county voter turnout and percentages were:
        - Jefferson produced 10.5% of the turnout and *38,855* votes.
        - Denver produced 82.8% of the turnout and *306,055* votes.
        - Arapahoe produced 6.7% of the turnout and *24,801* votes.

        (See the .txt output below:)

        [County_Votes.png](https://github.com/hillmanj1995/Election_Analysis/blob/main/Resources/County_Votes.png)

    - The following excerpts of code were used to determine those values ("..." signifies portions of code that do not directly apply to the method in question):

          '# 1: Create a county list and county votes dictionary.            
            county_options = []
            county_votes = {}

          '# 2: Track the largest county and county voter turnout.  
            largest_county = ""
            county_voter_turnout = 0

          ...
           
           #For each row in the CSV file.           
           for row in reader:

            ...

                # 3: Extract the county name from each row.                
                county_name = row[1]

                # 4a: Write an if statement that checks that the
                # county does not match any existing county in the county list.
                
                if county_name not in county_options:

                    # 4b: Add the existing county to the list of counties.                   
                    county_options.append(county_name)

                    # 4c: Begin tracking the county's vote count.                    
                    county_votes[county_name] = 0

                    # 5: Add a vote to that county's vote count.                   
                    county_votes[county_name] += 1
    
            ...

          #6a: Write a for loop to get the county from the county dictionary.
          for county in county_votes:
            
            # 6b: Retrieve the county vote count.
            county_vote_count = county_votes[county]
            
            # 6c: Calculate the percentage of votes for the county.
            county_vote_percentage = float(county_vote_count) / float(total_votes) * 100

            # 6d: Print the county results to the terminal.
            county_results = (
                f"{county}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
            print(county_results)
          
            #6e: Save the county votes to a text file.
            txt_file.write(county_results)

            

- Largest county voter turnout:

    - The county with the largest voter turnout was Denver, with *306,055* votes and 82.8% of the total voter turnout (see .txt output below):

        [Largest_County_Turnout.png](https://github.com/hillmanj1995/Election_Analysis/blob/main/Resources/Largest_County_Turnout.png)

    - The following excerpts of code were used to determine that value ("..." signifies portions of code that do not directly apply to the method in question):
        
          '...

                #6f: Write an if statement to determine the winning county and get its vote count.
                if (county_vote_count > county_voter_turnout):
                    county_voter_turnout = county_vote_count
                    largest_county = county
        
          #7: Print the county with the largest turnout to the terminal.
          county_summary = (
             f"\n----------------------------\n"
             f"Largest County Turnout: {largest_county}\n"
             f"----------------------------\n")
          
          print(county_summary)
        
          #8: Save the county with the largest turnout to a text file.
          txt_file.write(county_summary)

- Candidates results:

    - The candidate vote turnout and percentages were:
        - Charles Casper Stockham: 23.0% (*85,213*)
        - Diana DeGette: 73.8% (*272,892*)
        - Raymon Anthony Doane: 3.1% (*11,606*)
    
        (See the .txt output below:)

        [Candidate_Results.png](https://github.com/hillmanj1995/Election_Analysis/blob/main/Resources/Candidate_Results.png)

    - The following excerpts of code were used to determine those values ("..." signifies portions of code that do not directly apply to the method in question):

          '#Candidate Options and candidate votes.
          candidate_options = []
          candidate_votes = {}

          ...

          #Track the winning candidate, vote count and percentage
          winning_candidate = ""
          winning_count = 0
          winning_percentage = 0

          ...

          #For each row in the CSV file.
          for row in reader:

            ...

            #Get the candidate name from each row.
            candidate_name = row[2]

            #3: Extract the county name from each row.
            county_name = row[1]

            #If the candidate does not match any existing candidate add it to
            #the candidate list
            if candidate_name not in candidate_options:

                # Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)

                # And begin tracking that candidate's voter count.
                candidate_votes[candidate_name] = 0

          #Add a vote to that candidate's count
          candidate_votes[candidate_name] += 1

          ...

          #Save the final candidate vote count to the text file.
          for candidate_name in candidate_votes:
                
            #2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
                
            #3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
        
            #To do: print out each candidate's name, vote count, and percentage of
            #votes to the terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            #Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
        
            #Save the candidate results to our text file.
            txt_file.write(candidate_results)

- Winner Summary:

    - The winner of the election was Diana Degette, with a vote count of *272,892* which was 73.8% of the total votes (see .txt output below):

         [Winner_Data.png](https://github.com/hillmanj1995/Election_Analysis/blob/main/Resources/Winner_Data.png)

    - The following excerpts of code were used to determine those values ("..." signifies portions of code that do not directly apply to the method in question):

          '...
          
          # Determine winning vote count, winning percentage, and candidate.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
                
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

          # Print the winning candidate (to terminal)
          winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
          print(winning_candidate_summary)

          # Save the winning candidate's name to the text file
          txt_file.write(winning_candidate_summary)

## Election Summary

The analyst successfully created a script that can analyze the election data that Tom and his manager need to provide a conclusive result.  This script operates in such a way that with a few modifications, it can analyze smaller/larger data sets and/or retrieve different data from the imported file.  

### Examples:
- If the dataset were to be larger/include more columns of data, the same loop structure could be utilized to analyze those additional columns and provide further info the results.  This would be useful if the data set further broke down the votes into districts.
- If Tom and his manager wanted to check that there were no duplicate ballot ID's, they could use the section of code similar to the section where the analyst checked to see if the candidate names matched any of the previous names in the list as the script ran through its rows.  If the name didn’t match anything previous, it would be added to the list.  They would add a line of code to get the ballot Id from each row, run the loop, then get a count the number of ballot ID's and compare that to the count in the dataset. 
