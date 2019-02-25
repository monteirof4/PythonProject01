#Import OS Module
import os
#Import CSV module
import csv

#Direct to CSV path with raw data
csv_path = os.path.join('Resources','budget_data.csv')

#Define output file path
output_file = os.path.join('Resources',"financial_analysis.txt")

#open CSV file
with open(csv_path, newline='') as csvfile:
    #make CSV reader
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header
    next(csvreader)
    
    #create lists to store file data
    months = []
    profitloss = []
    plchange =[]
    
    #read first row with data to not calculate Profit/Losses change
    row = next(csvreader)
    months.append(row[0])
    profitloss.append(int(row[1]))
    plchange.append(0)
    pllstatmonth = int(row[1])
    
    #Read file and store data in lists
    for row in csvreader:
       months.append(row[0])
       profitloss.append(int(row[1]))
       plchange.append(int(row[1])-pllstatmonth)
       pllstatmonth = int(row[1])
    
#Print out results to terminal and to text file
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {len(months)}')
print(f'Total: ${sum(profitloss)}')
averagechange = sum(plchange)/(len(months)-1)
print(f'Average Change: ${round(averagechange,2)}')
greatestinc = max(plchange) #Finding Greatest Increase in profits
greatestincmonth = months[plchange.index(greatestinc)] #Finding the month of the Greatest Increase
greatestdec = min(plchange) #Finding Greatest Decrease in profits
greatestidecmonth = months[plchange.index(greatestdec)] #Finding the month of the Greatest Decrease
print(f'Greatest Increase in Profits: {greatestincmonth} (${greatestinc})')
print(f'Greatest Decrease in Profits: {greatestidecmonth} (${greatestdec})')

#Print out results to text file
with open(output_file, 'w') as text:

    text.write('Financial Analysis\n')
    text.write('----------------------------\n')
    text.write(f'Total Months: {len(months)}\n')
    text.write(f'Total: ${sum(profitloss)}\n')
    text.write(f'Average Change: ${round(averagechange,2)}\n')
    text.write(f'Greatest Increase in Profits: {greatestincmonth} (${greatestinc})\n')
    text.write(f'Greatest Decrease in Profits: {greatestidecmonth} (${greatestdec})\n')
