# create a dataset 
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
profits = []
months = []


# open the file using "write" mode. Specify the variables to hold the contents
with open(csvpath) as csvfile:

    #Initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader)
    
    for rows in csvreader:
        
        profits.append(int(rows[1]))
        months.append(rows[0])
        sum_profits = sum(profits)
        row_count =len(months)
        
    print(str(sum_profits))

# average change in profit loss between months
    n=0
    i=0
    loss=[]
    num = 0
    for x in range(len(profits)-1):
        
        loss.append(profits[n+1] - profits[n])
        n = n + 1
        
    average_change = sum(loss)/row_count
    
    # the average_change = number / row_count
    
    #write and solve cvswritermfor all rows 
    #cvswriter.writer (['.............'])
   # cvswriter.writer({'Total Months: ' + str(row_count)})
   #cvswriter.writer(['Total: $' + str(average_change]))
   #cvswriter.writer({'Average Change: " +str(average_change)})
   #cvswriter.writer({'Greatest Increase in Profits:' + str(month_max_value) +""+ str(max_value)})
   #cvswriter.writer(['Greatest Decreas in Profits: ' + str(month_min_value) +"" + str(min_value)])
    Output ={}
    Output = {"Financial Analysis", 
              "Total Months: {rows_count}\n",
              "Total: $ {total}\n",
              "Greatest Increase in Profits: {months_max_value} {max_value\}",
              "Greatest Decrease in Profits: {months_min_value} {Min_value}"}
   
    
    print("Financial Analysis")
    print('......................')
    print(f'Total Months: {row_count}')
    print ("Total: $" + str(sum_total))
    print(f'Average Change: {average_change}')
    print(f'Greatest Increase in Profits: {months_max_value} {max_value}')
    print(f'Greatest Decrease in Profits: {months_min_value} {min_value}')
    