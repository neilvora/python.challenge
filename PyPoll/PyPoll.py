import os
import csv

filepath = os.path.join("Resources","Pypoll.csv")

# Set Variables

total_votes_cast = 0
candidate = "null"
candidates = []
candidates_votes = {}
percentage_votes_won = {}




# First loop to generate candidates list and total votes 

with open(filepath) as PyPoll:
    csvfile = csv.reader(PyPoll)

    header_row = next(csvfile)

    first_row = next(csvfile)
    total_votes_cast = 1
    candidates.append(first_row[2])

    for row in csvfile:
        total_votes_cast = total_votes_cast + 1
        candidate = row[2]
        if not candidate in candidates:
            candidates.append(candidate)


# Set key values to 0 for candidates_votes{} and percentage_votes_won{} dictionaries
# Candidate names = key, votes = value
# Iterate on candidates list to generate key value pairs for dictionary candidates_votes{}

for i in candidates:
    candidates_votes[i]= 0
    percentage_votes_won[i] = 0

with open(filepath) as PyPoll:
    csvfile = csv.reader(PyPoll)

    header_row = next(csvfile)

    for row in csvfile:
        for i in candidates:
            if row[2] == i:
                candidates_votes[i] = candidates_votes[i] + 1


# Iterate on candidates list to generate key value pairs for dictionary percentage_votes_won{}

for i in candidates:
    percentage_votes_won[i] = (round(candidates_votes[i]/total_votes_cast * 100,3))




print(f'Election Results')
print(f'-----------------------------')
print(f'Total Votes: {total_votes_cast}')
print(f'-----------------------------')
for i in candidates:
    print(f'{i}: {percentage_votes_won[i]}% ({candidates_votes[i]} Votes)')
print(f'-----------------------------')

winner = max(candidates_votes, key=candidates_votes.get)

print(f'Winner: {winner}')

txtpath = os.path.join("Resources","Results_Pypoll.txt")

with open(txtpath,'w') as txtfile:
    txtfile.write(
    f'Election Results\n' 
    f'-----------------------------\n'
    f'Total Votes: {total_votes_cast}\n'
    f'-----------------------------\n')

    for i in candidates:
        txtfile.write(f'{i}: {percentage_votes_won[i]}% ({candidates_votes[i]} Votes)\n')
    
    txtfile.write(
    f'-----------------------------\n'
    f'Winner: {winner}\n'
    )

    txtfile.close()


















    