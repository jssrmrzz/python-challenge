import os
import csv

filepath = os.path.join('Resources', 'election_data.csv')

# Set Variables
votelist = []

candids = []
pctcandid = []
countcandid = []

totalvote = 0
with open(filepath, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')

    #Skips Header
    next(csv_reader)

    for row in csv_reader:
        votelist.append(row[2])

totalvote = len(votelist)
   
 #   
for name in votelist:
    if name not in candids:
        candids.append(name)
        x = name

count = 0

candid =  votelist[0]

lastcount = 0

print("Election Results")
print("-------------------------")
print("Total Votes:", totalvote)
print("-------------------------")


for candid in candids:
    for vote in votelist:
        if candid == vote:
            count += 1
    percent = count / len(votelist)
    pctcandid.append(percent)
    countcandid.append(count)

    if lastcount < count:
        Winner = candid
    print(f"{candid}: {pctcandid} ({count})")

lastcount = 0
count = 0

print("-------------------------")
print("Winner:", candid)
print("-------------------------")
