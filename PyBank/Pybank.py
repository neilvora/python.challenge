#Import Modules
import os
import csv

# Set File Path
filepath = os.path.join('Resources','budget_data.csv')

# Set Variables
total_months = 0
total_pl = 0
monthly_change = []
prior_month_value = 0
current_month_value = 0
net_change = 0
greatest_increase_month = 'Jan'
greatest_decrease_month = 'Jan'




# Open CSV file with csvreader

with open(filepath) as Pybank:
    csvfile =csv.reader(Pybank)

    header_row = next(csvfile)

    first_row = next(csvfile)
    total_months = 1
    current_month_value = int(first_row[1])
    total_pl = current_month_value
    

    for row in csvfile:
        #Store Prior Month Value
        prior_month_value = current_month_value
        # Iterate on total months value
        total_months = total_months + 1
        # Aggregate total PL
        total_pl = total_pl + int(row[1])
        # Calculate/Store Current Month Value
        current_month_value = int(row[1])
        # Calulate Net Change in PL
        net_change = current_month_value - prior_month_value
        # Store Net Change value in Monthly Change list
        monthly_change.append(net_change)

        # Find monthly values for max/min of monthly change list

        if net_change == max(monthly_change):
            greatest_increase_month = row[0]
        elif net_change == min(monthly_change):
            greatest_decrease_month = row[0]


average_monthly_change = round(sum(monthly_change)/len(monthly_change),2)
max_value_change = max(monthly_change)
min_value_change = min(monthly_change)




print(f'Total Months: {total_months}')
print(f'Total: ${total_pl}')
print(f'Average Change: ${average_monthly_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${max_value_change})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${min_value_change})')

txtpath = os.path.join('Resources','Results.txt')

with open(txtpath,'w') as txtfile:
    txtfile.write(
     f'Total Months: {total_months}\n' 
     f'Total: ${total_pl}\n' 
     f'Average Change: ${average_monthly_change}\n' 
     f'Greatest Increase in Profits: {greatest_increase_month} (${max_value_change})\n' 
     f'Greatest Decrease in Profits: {greatest_decrease_month} (${min_value_change})' 
    )
    txtfile.close()

