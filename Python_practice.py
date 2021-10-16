# 3.3.1 Import and Inspect the Data
import csv
import os


# # for i in os.listdir(r"c:/Users/mchauvet/..."):
# #     print(i)

file_to_load = os.path.join("c:/Users/mchauvet/Desktop/BC_2/03.Python/Election_Analysis/Resources/election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("c:/Users/mchauvet/Desktop/BC_2/03.Python/Election_Analysis/analysis/election_analysis.txt")

#Using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file
#     txt_file.write("Counties in the Election\n_ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")


with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # To do: read and analyze the data here
    # for row in file_reader:
    #     print(row)

    #print the header row
    headers = next(file_reader)
    print(headers)


