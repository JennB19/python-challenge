import os
import csv
# Objective 2: Set the path for the CSV file in PyPollcsv
PyPollcsv = os.path.join("Resources","election_data.csv")
# Objective 3: Create the lists to store data. Initialize
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []
# Open the CSV using the set path PyPollcsv
with open(PyPollcsv, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)
   # Conduct the ask
   for row in csvreader:
       # Count the total number of votes
       count = count + 1
       # Set the candidate names to candidatelist
       candidatelist.append(row[2])
       # Create a set from the candidatelist to get the unique candidate names
   for x in set(candidatelist):
       unique_candidate.append(x)
       # y is the total number of votes per candidate
       y = candidatelist.count(x)
       vote_count.append(y)
       # z is the percent of total votes per candidate
       z = (y/count)*100
       vote_percent.append(z)
   winning_vote_count = max(vote_count)
   winner = unique_candidate[vote_count.index(winning_vote_count)]

#  str(round(answer, 2))Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) Tried rounding and that didn't work yet.
print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes :" + str(count))
print("-------------------------")
for i in range(len(unique_candidate)):
           print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Specify the file to write to
output_path = os.path.join("Resources" , "new.csv")
with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the first row (column headers)
    csvwriter.writerow(['Voter ID', 'County', 'Candidate'])
