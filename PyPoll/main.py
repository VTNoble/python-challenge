# import csv and os
import csv
import os

# set up file path to access csv file
csvpath = os.path.join("Resources", "election_data.csv")

# open the csv file
with open(csvpath, encoding='utf') as csvfile:

    # read in the csv file
    election_data = csv.reader(csvfile, delimiter=',')

    # extract the header
    csvheader = next(election_data)

    # set up list to count votes for each candidate
    # looking at the dataset, we know there are only 3 candidates who received votes
    # vote breakdown will use the format [Stockham, DeGette, Doane]
    vote_breakdown = [0, 0, 0]

    # list of candidates
    candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]

    # set up variable to track total votes and initialize at 0
    # we will also use this as a quick check to confirm the sum of vote_breakdown is equal to the total votes
    total_votes = 0

    # loop through votes
    for vote in election_data:

        # add vote to total votes
        total_votes += 1

        # evaluate each vote and add vote to corresponding candidate in vote_breakdown
        if vote[2] == candidates[0]:
            vote_breakdown[0] += 1
        elif vote[2] == candidates[1]:
            vote_breakdown[1] += 1
        elif vote[2] == candidates[2]:
            vote_breakdown[2] += 1

    # this is a check to make sure the assumptions were correct regarding only 3 candidates receiving votes
    # uncomment lines 44 and 45 to perform check
    #if total_votes == sum(vote_breakdown):
        #print(True)

    # list comprehension to calculate and generate list of percentages and round to 3 digits
    vote_percentages = [round(votes / total_votes * 100,3) for votes in vote_breakdown]

    # find winner or determine if there is a tie
    winner = ""
    if vote_breakdown[0] > vote_breakdown[1] and vote_breakdown[0] > vote_breakdown[2]:
        winner = candidates[0]
    elif vote_breakdown[1] > vote_breakdown[0] and vote_breakdown[1] > vote_breakdown[2]:
        winner = candidates[1]
    elif vote_breakdown[2] > vote_breakdown[0] and vote_breakdown[2] > vote_breakdown[1]:
        winner = candidates[2]
    else:
        print("There is a tie!")

# specify output path
output_path = os.path.join("analysis", "results.txt")

# lines to print to txt file
lines = ["--------------------------", "Election Results", "--------------------------", f"Total Votes: {total_votes}", "--------------------------", f"{candidates[0]}: {vote_percentages[0]}% ({vote_breakdown[0]})", f"{candidates[1]}: {vote_percentages[1]}% ({vote_breakdown[1]})", f"{candidates[2]}: {vote_percentages[2]}% ({vote_breakdown[2]})", "--------------------------", f"Winner: {winner}", "--------------------------"] 

# open the file using "write" mode
with open(output_path, 'w') as results:

    # loop through list of lines and write to file
    for line in lines:
        results.write(line)
        results.write("\n")

# print results to terminal
for line in lines:
    print(line)

