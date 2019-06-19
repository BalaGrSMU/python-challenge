import os
import csv
candidate=[]
county=[]
unique_candidate=[]
vote_percent = []
vote_count = []


#initializing variables
# count number of rows
count=0


csvpath = os.path.join('..','Resources','election_data.csv')
with open(csvpath, newline="") as csvfile:
   csvreader = csv.reader(csvfile,delimiter = ',')
   csv_header = next(csvreader)
   for row in csvreader:
       count = count + 1
       candidate.append(row[2])
       county.append(row[1])
   for x in set(candidate):
       unique_candidate.append(x)
       y=candidate.count(x)
       vote_count.append(y)
       z = round((y/count)*100,2)
       vote_percent.append(z)
       winning_vote_count = max(vote_count)
       winner = unique_candidate[vote_count.index(winning_vote_count)]
print("The total votes polled : " + str(count) + "\n")
for i in range(len(unique_candidate)):
    print(unique_candidate [i] + ": " + str(vote_percent[i]) + ": " + str(vote_count[i]) + "\n")
print("The winner is :" + winner)

filepath = os.path.join("..", "Resources","poll_output.csv")
with open(filepath,'w') as text:
    text.write("The total votes polled : " + str(count) + "\n")
    for i in range(len(unique_candidate)):
        text.write(unique_candidate [i] + ": " + str(vote_percent[i]) + ": " + str(vote_count[i]) + "\n")
    text.write("The winner is :" + winner + "\n")