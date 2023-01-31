#import dependencies
import os
import csv

#Read in the Budget_Data Csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#set initial variables and values
def read_csv(csvpath):

    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
    #Include & Print the Header
        csv_header = next(csvreader)
        data=[]
        
        #loop through file 
        for row in csvreader:
            data.append(row)
    return(data)

#add total number of months       
def total_months(data):
        #row_number = 0 
        #for row in data: 
        #   row_number += 1
        #return row_number

    return len(data)


#add total net profit/loss amount for the entire time period

def total_profit_loss(data):
    profit_loss = 0
    for row in data:
        profit_loss += int(row[1])
    return profit_loss

#Calculate the change in profit (date and amount) over the entire period.

def change_in_profit(data):
    first_month_profit = int(data[0][1])
    last_month_profit = int(data[-1][1])
    return first_month_profit - last_month_profit


#Calculate the greatest increase in profits (date and amount)over the entire period 

def change_in_profit_list(data):
    changes_in_profit = []
    first_row = int(data[0][1])
    for row in data[1:]:
        current_row = int(row[1])
        change = current_row - first_row
        changes_in_profit.append(change)
        first_row = current_row
    return changes_in_profit

def avg_of_list(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)

#Calculate greatest decrease in profits (date and time) over the entire period.
def greatest_inc(list_of_changes):
    greatest_inc = max(list_of_changes)

    return [greatest_inc]

def greatest_dec (list_of_changes):
    greatest_dec = min(list_of_changes)

    return[greatest_dec]


#Print the results using a variable for the csv
data = read_csv(csvpath)
print("Financial Analysis")
print("-------------------------")
print("Total Months: ", total_months(data))
print(f"Total: ${total_profit_loss(data)}")
changes = change_in_profit_list(data)
print(f"Average Change: S{round(avg_of_list(changes), 2)}")
print(f"Greatest increase in profits: {greatest_inc(changes)}")
print(f"Greatest decrease in profits: {greatest_dec(changes)}")



#Set variable for output file
output_file = os.path.join("Resources", "budget_data.csv")

# zip the rows to put into the output file
zipped_rows = [total_months(data), total_profit_loss(data), change_in_profit_list(data), round(avg_of_list(changes), 2), 
greatest_inc(changes), greatest_dec(changes)]

#  Open the output file
with open(csvpath, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row

    writer.writerow(["Total Months", "Total", "Average Change", "Greatest Increase","Greatest Decrease"])

    # Write in zipped rows

    writer.writerows([zipped_rows])










  

        
        
              




        
        
        
        
        
       







