import csv
import os

# # for i in os.listdir(r"c:/Users/mchauvet/..."):
# #     print(i)

file_to_load = os.path.join("c:/Users/mchauvet/Desktop/BC_2/03.Python/Election_Analysis/Resources/election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("c:/Users/mchauvet/Desktop/BC_2/03.Python/Election_Analysis/analysis/election_analysis.txt")

#Using the with statement open the file as a text file
# With open(file_to_save, "w") as txt_file:

#     # Write some data to the file
#     txt_file.write("Counties in the Election\n_ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

# 1.Initialize a accomulator variable, candidate options variable, etc
total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#This with statemen is for have total_votes, candidate_options and candidate_votes
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Skip the header row
    headers = next(file_reader)
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        #If conditionals
        if candidate_name not in candidate_options:
            #Add the candidate name to a candidate list
            candidate_options.append(candidate_name)
            #Begin tracking thata candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#This for statement is for have the percentage of votes
#We need the formula: vote_percentage = votes (float) / total_votes (float) * 100
for candidate_name  in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes ) / float (total_votes) * 100
    #print(f'{winning_candidate} won for this: {winning_count} {winning_percentage}')
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
#Print winning candidate information
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)
 
