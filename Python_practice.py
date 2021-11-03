import csv
import os


#Create a filename variable to a direct or indirect path to the file.
file_to_load = os.path.join("c:/Users/mchauvet/Desktop/BC_2/03.Python/Election_Analysis/Resources/election_results.csv")
file_to_save = os.path.join("c:/Users/mchauvet/Desktop/BC_2/03.Python/Election_Analysis/analysis/election_analysis.txt")

#Initialize accumulator variables.
total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#This with statemen is for have total_votes, candidate_options and candidate_votes.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Skip the header row
    headers = next(file_reader)
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            #Add the candidate name to a candidate list
            candidate_options.append(candidate_name)
            #Begin tracking thata candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #This for statement is for have the percentage of votes
    #We need the formula: vote_percentage = votes (float) / total_votes (float) * 100
    for candidate_name  in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes ) / float (total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
    
# Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)