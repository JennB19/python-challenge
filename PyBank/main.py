import os
import csv
#Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
#print(csvpath)
# Open and read the CSV
with open(csvpath, newline="") as csvfile:
   #print(csvreader)
   # Read header row, print it, set it aside
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvfile)
   #print(f"Header: {csv_header}")
   # Declare variables as empty lists
   Months = []
   Profit_Loss = []
   Differences = []
   Greatest_Increase_Date = ""
   Greatest_Decrease_Date = ""
   # Count total number of months the data encapsulates
   for row in csvreader:
       Months.append(row[0])
       Profit_Loss.append(int(row[1]))
   # Print Statements
   print("Financial Analysis")
   print("-------------------------------")
   print("Total Months: ", len(Months))
   print("Net Total: $", sum(Profit_Loss))
   for i in range(1, len(Profit_Loss)):
       # Find average change between months
       Differences.append(Profit_Loss[i] - Profit_Loss[i-1])
       # Find average of values
       Average_Change = sum(Differences) / len(Differences)
       # Determine greatest increase and date
       Greatest_Increase = max(Differences)
       Greatest_Increase_Date = str(Months[Differences.index(max(Differences))])
       # Determine greatest decrease and date
       Greatest_Decrease = min(Differences)
       Greatest_Decrease_Date = str(Months[Differences.index(min(Differences))])
   # Print Statements
   print("Average Change: $", round(Average_Change))
   print("Greatest Increase: ", Greatest_Increase_Date, "($", Greatest_Increase,")")
   print("Greatest Decrease: ", Greatest_Decrease_Date, "($", Greatest_Decrease,")")

# Specify the file to write to
output_path = os.path.join("Resources" , "new.txt")
with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the first row (column headers)
    csvwriter.writerow(['Data', 'Profit/Losses'])
