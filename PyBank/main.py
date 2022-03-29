# import csv and os
import csv
import os

# set up file path to access csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# open the csv file
with open(csvpath, encoding='utf') as csvfile:
    
    # read in file using csv module
    budget_data = csv.reader(csvfile, delimiter=',')

    # extract the header
    csvheader = next(budget_data)

    # extract first row of data to be assigned to variables below:
    csvfirst = next(budget_data)
    
    # declare variable for total months and initialize at 1 to include first row extracted above
    total_months = 1

    # declare variable for net profit and initialize at value from first row
    net_profit = int(csvfirst[1])

    # previous month variable initialized at value from first row
    previous_month = int(csvfirst[1])

    # declare variables to track greatest increase and decrease over the entire period
    greatest_inc = 0
    greatest_inc_date = " "
    greatest_dec = 0
    greatest_dec_date = " "

    # set up list of monthly changes
    monthly_change_list = []

    # loop through data
    for row in budget_data:
        
        # add 1 to total months
        total_months += 1

        # update net_profit
        net_profit += int(row[1])

        # set up monthly change variable and calculate difference from current month and previous month
        monthly_change = int(row[1]) - previous_month

        # append monthly change to list
        monthly_change_list.append(monthly_change)

        # check if monthly change is greater than current greatest increase
        if monthly_change > greatest_inc:
            # if so, update greatest variables
            greatest_inc = monthly_change
            greatest_inc_date = row[0]
        
        # check if monthly change is greater than current greatest decrease
        if monthly_change < greatest_dec:
            # if so, update greatest variables
            greatest_dec = monthly_change
            greatest_dec_date = row[0]

        # reassign previous_month variable prior to loop progressing to next row
        previous_month = int(row[1])

    # calculate average monthly change
    average_change = round(sum(monthly_change_list) / (total_months - 1), 2)

# specify output path
output_path = os.path.join("analysis", "results.txt")

# list of lines to write to report
lines = ["--------------------------", "Financial Analysis Report", "--------------------------", f"Total Months: {total_months}", f"Total: {net_profit}", f"Average Change: {average_change}", f"Greatest Increase in Profits: {greatest_inc_date} ({greatest_inc})", f"Greatest Decrease in Profits: {greatest_dec_date} ({greatest_dec})", "--------------------------", "End of Report", "--------------------------"]

# open the file using "write" mode
with open(output_path, 'w') as results:

    # loop through list of lines and write to file
    for line in lines:
        results.write(line)
        results.write("\n")

# print report to terminal
for line in lines:
    print(line)
