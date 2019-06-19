import os
import csv
date=[]
profit=[]
monthlyChanges=[]

#initializing variables
# count number of rows
count=0
# cumulative of profits
totalProfit=0
# change in profit
totalChangeProfits=0
# starting profit
initialProfit=0

csvpath = os.path.join('..','Resources','budget_data.csv')
with open(csvpath, newline="") as csvfile:
   csvreader = csv.reader(csvfile,delimiter = ',')
   csv_header = next(csvreader)
   for row in csvreader:
       count = count + 1
       date.append(row[0])

       profit.append(row[1])
       totalProfit=totalProfit+int(row[1])
       finalProfit=int(row[1])       
       monthlyProfitChange = finalProfit - initialProfit
       monthlyChanges.append(monthlyProfitChange)
       
       totalChangeProfits= totalChangeProfits+ monthlyProfitChange
       initialProfit=finalProfit
       changecount = int(count)-1
       changeprofit= (totalChangeProfits - monthlyChanges[0])
       #averageChangeProfit = round((totalChangeProfits - monthlyChanges[0])/count,2)
       maxIncProfit = max(monthlyChanges)
       minIncProfit = min(monthlyChanges)
       inc_date = date[monthlyChanges.index(maxIncProfit)]
       dec_date = date[monthlyChanges.index(minIncProfit)]
   print("________________________________")
   print("Financial Analysis")
   print("________________________________")
   print("The total number of months included in the dataset: ", count)
   print("The total net amount of Profits/Losses is ", str(totalProfit) )
   print("Total Change Profits "+ str(totalChangeProfits-monthlyChanges[0]))
   print("Average change proift" + str(changeprofit/changecount))
   print("Greatest Increase in Profits " + "$" + str(maxIncProfit) + " in " + str(inc_date))
   print("Greatest Decrease in Profits " + "$" + str(minIncProfit) + " in " + str(dec_date))
   print("________________________________")

   filepath = os.path.join("..", "Resources","bank_output.csv")
   with open(filepath,'w') as text:
        text.write("Financial Analysis" + "\n")
        text.write("----------------------------------------" + "\n")
        text.write(f"The total number of months included in the dataset:  {count}" + "\n")
        text.write(f"The total net amount of Profits/Losses:  {totalProfit}" + "\n")
        text.write(f"Total Change Profits: ${totalChangeProfits - monthlyChanges[0]}" + "\n")
        text.write(f"Average change profit: : ${changeprofit/changecount}" + "\n")
        text.write(f"Greatest Increase in Profits: ($ {maxIncProfit} {inc_date})" + "\n")
        text.write(f"Greatest Decrease in Profits: ($ {minIncProfit} {dec_date})" + "\n") 