import os
import csv
print("Financial Analysis")
print("-----------------------------------")
filepath = os.path.join('Instructions/PyBank/Resources/budget_data.csv')
# Total month
month = 0
with open(filepath, newline='') as the_file1:
   csv_reader = csv.reader(the_file1)
   #csv_reader = next(csv_reader)
   for row in csv_reader:
       month += 1
   print(f'Total Months : {month}')
# Netloss or Profit?
total = 0
row_index_profit =1
with open(filepath, newline='') as the_file2:
   csv_reader_object = csv.reader(the_file2)
   if csv.Sniffer().has_header:
       next(csv_reader_object)
   for row in csv_reader_object:
       float_profit = int(row[row_index_profit])
       total += float_profit
   print(f'Total: ${total}')
# Average Change
with open(filepath, newline='') as the_file3:
   csvreader = csv.reader(the_file3, delimiter=',')
   csv_header = next(csvreader)
   P = []
   months = []
   for rows in csvreader:
       P.append(int(rows[1]))
       months.append(rows[0])
   revenue_change = []
   for x in range(1, len(P)):
       revenue_change.append((int(P[x]) - int(P[x-1])))
   # Net total amount change
   revenue_average = round(sum(revenue_change) / len(revenue_change),2)
   # Greatest increase in profit
   greatest_increase = max(revenue_change)
   # Greatest decrease in loss
   greatest_decrease = min(revenue_change)
print(f'Average Change:${revenue_average}')
print(f'Greatest Increase in Profits: {months[revenue_change.index(max(revenue_change))+1]} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {months[revenue_change.index(min(revenue_change))+1]} (${greatest_decrease})')