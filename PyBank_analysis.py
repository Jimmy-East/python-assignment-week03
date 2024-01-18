#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Modules
import os
import csv

# Set path for file
csv_path = os.path.join('Starter_Code', 'PyBank', 'Resources', 'budget_data.csv')

# Initialize variables
months_total = 0 
total_profit = 0 
previous_month_profit_loss = 0
total_change = 0
greatest_increase_month = ""
greatest_decrease_month = ""
greatest_increase_value = 0
greatest_decrease_value = 0

with open(csv_path) as csv_file :
    
    #read file
    csv_budget_data = csv.reader(csv_file, delimiter = ',')

    # printing headers on file
    budget_data_header = next(csv_budget_data)

    # looping to through the csv files contents
    for row in csv_budget_data:
        months_total+= 1
        total_profit += int(row[1])
        
        
        if months_total > 1:
            current_month_profit_loss = int(row[1])
            change = current_month_profit_loss - previous_month_profit_loss
            total_change += change
            
            # Check for the greatest increase
            if change > greatest_increase_value:
                greatest_increase_value = change
                greatest_increase_month = row[0]  # Assuming the first column contains month values

            # Check for the greatest decrease
            if change < greatest_decrease_value:
                greatest_decrease_value = change
                greatest_decrease_month = row[0]
            
        # Set the current month's profit/loss as the previous month for the next iteration
        previous_month_profit_loss = int(row[1])
        
# Calculate the average change
average_change = round(total_change / (months_total - 1), 2)

       
    # Print the total number of months
    
print('Financial Analysis')
print("")
print("--------------------------------------")
print("")
print(f"Total Months: {months_total}")
print("")
print(f"Total: ${total_profit}")
print("")
print(f"Average Change: ${average_change}")
print("")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_value})")
print("")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_value})")
print("")

# Set path for output file
output_path = os.path.join('PyBank_Financial_Analysis.txt')

# Open the file in write mode and write the results
with open(output_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("=============================\n")
    output_file.write(f"Total number of months: {months_total}\n")
    output_file.write(f"Total profit/loss: ${total_profit}\n")
    output_file.write(f"Average change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_value})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_value})\n")


# In[ ]:




