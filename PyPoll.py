# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
# file_to_load = "Resources\election_results.csv"
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Reset total vote counter
total_votes = 0

# Declare candidate list
candidate_options = []

# Create candidate vote counter
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load, 'r', encoding='utf8') as election_data:
    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # skip the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Accumulate total vote counter
        total_votes += 1
        # read candidate name
        candidate_name = row[2]
        # verify if candidate name is not included in the candidate list
        if candidate_name not in candidate_options:
            # Add candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Start vote counter for candidate
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Save results to a txt file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n"
    )
    print(election_results, end="")
        
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # determine the percentage of votes for each candidate
    # read through each candidate in the dictionary
    for candidate_name in candidate_votes :
        # Retrieve candidate vote
        votes = candidate_votes[candidate_name]
        # Calculate percentage
        vote_percentage = votes / total_votes * 100
        # print the candidate name and percentage of votes
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)       