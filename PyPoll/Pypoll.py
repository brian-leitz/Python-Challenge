#import dependencies

import os
import csv

#set initial variables and values


def read_a_csv(csvpath):
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        #include the header
        csv_header = next(csvreader)
        data = []
        for row in csvreader:
            data.append(row)
    return data

#set variable for number of candidate votes
def count_candidate_votes(data):
    candidate_vote_count = {}

    #loop through the file to count candidate votes
    for row in data:
        candidate_name = row[2]
        if candidate_name in candidate_vote_count:
            candidate_vote_count[candidate_name] += 1
        else:
            candidate_vote_count[candidate_name] = 1
    return candidate_vote_count

#read in the csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#save the file in a variable
data = read_a_csv(csvpath)
#create a variable for the number of votes 
vote_counts = count_candidate_votes(data)
#create a variable for the total amount of votes
total_votes = sum(vote_counts.values())
#print(total_votes)
#print number of votes and percentage of votes per candidate
#print the winner

# Building formatted output
line = "---------------"
print(line)
print("ELECTION RESULTS")
print(line)
print(f"Total Votes: {total_votes}")
print(line)
winning_total = 0
for key, value in vote_counts.items():
    print(f"{key}: {value} ({round((value/total_votes) * 100, 3)}%)")
    if value > winning_total:
        winning_total = value
        winning_candidate = key
print(line)
print(f"WINNER: {winning_candidate} with {winning_total} votes")

#Set variable for output file
output_file = os.path.join("Resources", "budget_data.csv")

# zip the rows to put into the output file
zipped_rows = ['369711', '85213', '272892', '11606', "Diana DeGette"]

#  Open the output file
with open(csvpath, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row

    writer.writerow(["Total Votes", "Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane","Winner"])

    # Write in zipped rows

    writer.writerows([zipped_rows])








