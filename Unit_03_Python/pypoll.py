import os
import csv

print("Election Results")
print("-----------------------------------")

filepath = os.path.join('Instructions/PyPoll/Resources/election_data.csv')

# Total Voters
voters = 0
with open(filepath, newline='') as the_file1:
   csv_reader = csv.reader(the_file1)
   csv_header = next(csv_reader)
   for row in csv_reader:
       voters += 1
   print(f'Total Votes : {voters}')

   
candidates = []
num_votes = []
percent_votes = []
# List of Candidates
voters= 0
with open(filepath, newline = "") as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ",")
   csv_header = next(csvreader)
   for row in csvreader:
       # Add to our vote-counter
       voters += 1
       
       if row[2] not in candidates:
           candidates.append(row[2])
           index = candidates.index(row[2])
           num_votes.append(1)
       else:
           index = candidates.index(row[2])
           num_votes[index] += 1

   # Add to percent_votes list
   for votes in num_votes:
       percentage = (votes/voters) * 100
       percentage = round(percentage)
       percentage = "%.3f%%" % percentage
       percent_votes.append(percentage)

   # Find the winning candidate
   winner = max(num_votes)
   index = num_votes.index(winner)
   winning_candidate = candidates[index]

# Displaying results
#print("Election Results")
#print("--------------------------")
#print(f"Total Votes: {str(voters)}")

print("--------------------------")
for i in range(len(candidates)):
   print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

#Place to save
txt_file = Path('python-challenge/PyPoll/PyPoll.txt')
with open(txt_file,"w") as txtfile:
#Write the result in txt file
   txtfile.write("Election Results")
   txtfile.write("\n")
   txtfile.write("-----------------------------------")
   txtfile.write("\n")
   txtfile.write(f'Total Votes : {voters}')
   txtfile.write("\n")
   txtfile.write("-----------------------------------")
   txtfile.write("\n")
   for i in range(len(candidates)):
       line = str(f"{candidates[i]}: {str(vote_percent[i])} ({str(vote_count[i])})")
       txtfile.write('{}\n'.format(line))
   txtfile.write("-----------------------------------")
   txtfile.write("\n")
   txtfile.write(f"Winner: {winner}")
   txtfile.write("\n")
   txtfile.write("-----------------------------------")