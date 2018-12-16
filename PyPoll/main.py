 # create a dataset 
import os
import csv

#csvpath = os.path.join()
#candidates = []
#andidate_votes = []


voterid = os.path.join("Resources", "election_data.csv")


# open the file using "write" mode. Specify the variables to hold the contents
with open(voterid) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # do not include headers
    csv_header = next(csvfile)
    
    #lists  and variables
    candidate =[]
    candidate_votes ={}
    total_votes = 0
    Percentage = 0
    winners = []
    
    
    

    #Initialize csv.reader
    #reader = csv.reader(election_data)
    #skip header
    #next(csvreader)
    
    
    for r in csvreader:
        total_votes = total_votes + 1
        candidate_name=r[2]
        if(candidate_name not in candidate):
            candidate.append(candidate_name)
            candidate_votes[candidate_name] = 0        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
       
