import os
import csv

filepath = os.path.join('Resources', 'budget_data.csv')


with open(filepath, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    
    #Skips Header
    next(csv_reader)
    
    # Setting Variables
    total_months = 0
    total = 0
    profloss = []
    monthlist = []
    monthchanges = []
    
    # Loop through whole file (Conditionals)
    for row in csv_reader:
        total_months+= 1
        total += int(row[1])
        profloss.append(row[1])
        monthlist.append(row[0])
    
   # 1st month profit/loss 
    oneprofloss = int(profloss[0])

    # Loop for monthly changes
    for i in range(1, len(profloss)):
       monthchanges.append(int(profloss[i]) - oneprofloss)
       oneprofloss = int(profloss[i])
       i += 1

    avgchange = sum(monthchanges) / len(monthchanges)

   # Seeks out Max/Min of monthly changes.
    maxincrease = max(monthchanges)
    maxdecrease = min(monthchanges)

   # Seeks out months with  Max Increase and Max Decrease 
    for i in range(len(monthchanges)):
        if monthchanges[i] == maxincrease:
            maxindex = (i + 1)
        elif monthchanges[i] == maxdecrease:
            minindex = (i + 1)
        else:
            i += 1

    maxmonth = monthlist[maxindex]
    minmonth = monthlist[minindex]
   
   
    # Print Results
    print("Financial Analysis")
    print("----------------------------") 
    print("Total Months:", total_months)
    print("Total:", total)
    #print("Average Change:", profloss)
    print("Average Change:", avgchange)
    print("Greatest Increase in Profits:", {maxmonth}, maxincrease)
    print("Greatest Decrease in Profits", {minmonth}, maxdecrease)

    
    

    

    


        


    
    





# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
  
          
