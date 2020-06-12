import os
import csv
path = os.path.abspath('C:/Users/li116/OneDrive/Desktop/python-Challenge/PyPoll/resource/election_data.csv')
with open(path,"r") as input_file:
     csvreader = csv.reader(input_file, delimiter=",")
     next(csvreader)
     #get number of votes cast
     voter_ID = []
     countries = []
     candidates = []
     for row in csvreader:
         voter = row[0]
         country = row[1]
         candiate = row[2]
         voter_ID.append(voter)
         countries.append(country)
         candidates.append(candiate)
         total = len(voter_ID)
     print("Election Results")
     print("---------------------------------------------------------")
     print("Total Votes: {}".format(total))

#the list of candidates who received votes
candidate_list =list(set(candidates))
print("---------------------------------------------------------")
#print(candidate_list)

#The percentage of votes each candiate won:

def candidate_percent(candi):
    list_candi = [candiate for candiate in candidates if candiate == candi]
    percent_0 = round(len(list_candi) * 100 / total, 3)
    return percent_0, len(list_candi)


print("{}: {}% ({})".format(candidate_list[0], candidate_percent(candidate_list[0])[0], candidate_percent(candidate_list[0])[1]))
print("{}: {}% ({})".format(candidate_list[1], candidate_percent(candidate_list[1])[0], candidate_percent(candidate_list[1])[1]))
print("{}: {}% ({})".format(candidate_list[2], candidate_percent(candidate_list[2])[0], candidate_percent(candidate_list[2])[1]))
print("{}: {}% ({})".format(candidate_list[3], candidate_percent(candidate_list[3])[0], candidate_percent(candidate_list[3])[1]))

print("---------------------------------------------------------")
max_vote = max(candidate_percent(candidate_list[0])[0], candidate_percent(candidate_list[1])[0], candidate_percent(candidate_list[2])[0], candidate_percent(candidate_list[3])[0])
for i in range(len(candidate_list)):
    if candidate_percent(candidate_list[i])[0] == max_vote:
        print("Winner: {}".format(candidate_list[i]))
        a = i


# export result to a text file
exportFile = open("analysis.txt","w")
A = "Election Results"
B = "--------------------------------"
C = "Total Votes: {}".format(total)
D = "{}: {}% ({})".format(candidate_list[0], candidate_percent(candidate_list[0])[0], candidate_percent(candidate_list[0])[1])
E = "{}: {}% ({})".format(candidate_list[1], candidate_percent(candidate_list[1])[0], candidate_percent(candidate_list[1])[1])
F = "{}: {}% ({})".format(candidate_list[2], candidate_percent(candidate_list[2])[0], candidate_percent(candidate_list[2])[1])
G = "{}: {}% ({})".format(candidate_list[3], candidate_percent(candidate_list[3])[0], candidate_percent(candidate_list[3])[1])
H = "Winner: {}".format(candidate_list[a])
exportFile.write(A + "\n" + B + "\n" + C + "\n" + B + "\n" + D + "\n" + E + "\n" + F + "\n" + G + "\n" + B + "\n" + H )
exportFile.close()
