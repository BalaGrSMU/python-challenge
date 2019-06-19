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
       
       
       output_file = os.path.join("bank_final.csv")
       cleaned_csv = zip(date, profit, monthlyChanges)
       with open(output_file, "w", newline="") as datafile:
            writer = csv.writer(datafile)
            writer.writerow(["Date", "Profit", "Monthly Changes"])
            writer.writerows(cleaned_csv)
       monthlyProfitChange = finalProfit - initialProfit
       monthlyChanges.append(monthlyProfitChange)
       number=len(monthlyChanges)
       for i in range(1,number):
        
        
        changecount = int(len(monthlyChanges)-1)
        totalChangeProfits= int(monthlyChanges[i])+totalChangeProfits
        totChange=totalChangeProfits
        initialProfit=finalProfit
        #changeprofit= (totalChangeProfits - monthlyChanges[0])
        #averageChangeProfit = round((totalChangeProfits - monthlyChanges[0])/count,2)
        averageChangeProfit = totChange/changecount
        maxIncProfit = max(monthlyChanges)
        minIncProfit = min(monthlyChanges)
        inc_date = date[monthlyChanges.index(maxIncProfit)]
        dec_date = date[monthlyChanges.index(minIncProfit)]
   print("________________________________")
   print("Financial Analysis")
   print("________________________________")
   print("The total number of months included in the dataset is ", count)
   print("The total rows in Monthly Profit Change is " + str(number))
   print("The total rows in change count is " + str(changecount))
   print("The total net amount of Profits/Losses is ", str(totalProfit) )
   print("The total change profits is " + str(totChange))
   #print("Total Change Profits "+ str(totalChangeProfits-monthlyChanges[0]))
   print("Average change profit " + str(totChange/changecount))
   #print("Average change profit " + str(averageChangeProfit))
   print("Greatest Increase in Profits " + "$" + str(maxIncProfit) + " in " + str(inc_date))
   print("Greatest Decrease in Profits " + "$" + str(minIncProfit) + " in " + str(dec_date))
   print("________________________________")