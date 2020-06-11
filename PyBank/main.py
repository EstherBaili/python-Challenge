import csv
import os
csvPath = os.path.abspath("C:/Users/li116/OneDrive/Desktop/python-Challenge/PyBank/resource/budget_data.csv")
with open(csvPath,"r") as input_csv_file:
    csvreader = csv.reader(input_csv_file, delimiter=",")
    #exclude header
    next(csvreader)
    #get months list
    months = [ ]
    amounts = [ ]
    dates = [ ]
    for row in csvreader:
        month = row[0].split("-")[0]
        amount = row[1]
        date = row[0]
        months.append(month)
        amounts.append(amount)
        dates.append(date)
    print(months, amounts, dates)

#get number of month
numMonths = len(months)
print("Total Months: {}".format(numMonths))

#get the total profit and loss
total = 0
for ele in range(0, len(amounts)):
    total = total + int(amounts[ele])
print("Total: ${}".format(total))

#the average of changes in p/l
averagePL = round((total / len(amounts)), 2)
print("Average Change: {}".format(averagePL))

#The greatest increase/decrease of profit
deltaPL = []
for ele in range(0, len(amounts)-1):
    delta = int(amounts[ele + 1]) - int(amounts[ele])
    deltaPL.append(delta)

maxPL = max(deltaPL)
minPL = min(deltaPL)

maxDate = dates[deltaPL.index(maxPL)+1]
minDate = dates[deltaPL.index(minPL)+1]
print("Greatest Increase in profits: {} (${})".format(maxDate, maxPL))
print("Greastest Decrease in Profits: {}(${})".format(minDate, minPL))


# export result to a text file
A = "Total Months: {}".format(numMonths)
B = "Total: ${}".format(total)
C = "Average Change: {}".format(averagePL)
D = "Greatest Increase in profits: {} (${})".format(maxDate, maxPL)
E = "Greastest Decrease in Profits: {}(${})".format(minDate, minPL)

exportFile = open("analysis.txt","w")
exportFile.write(A + "\n" + B + "\n" + C + "\n" + D + "\n" + E )
exportFile.close()


