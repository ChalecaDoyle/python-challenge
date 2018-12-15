 import os
 import csv
 
 # open the file using "write" mode. Specify the variables to hold the contents
with open(csvpath) as csvfile:
    
    total_votes = 0
    +vote_count =[]
    +1=[]
    
    #Get all input list of csv files in C:\Users\doyle\Desktop\python-challenge\PyPoll\Resources

    #Initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader) 
    
    for rows in csvreader:
        
        profits.append(int(rows[1]))
        months.append(rows[0])
        sum_profits = sum(profits)
        row_count =len(months)
        
    print(str(sum_profits))