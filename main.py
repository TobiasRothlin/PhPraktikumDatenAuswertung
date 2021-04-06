import csv

def printValueList(valList):
    print("lenght -> " + str(len(valList)))
    for line in valList:
        print(str(line[0]) + "\t\t\t\t |" + str(line[1]))
    return

def calculatePeriodicTime(file,nullValues):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='\n')
        ValueListRaw = []
        for row in spamreader:
            try:
                time = float(row[0])
                gyrY = float(row[2])
                ValueListRaw.append((time,gyrY))
            except:
                print(".")

    #printValueList(ValueListRaw)
    #print("----Done file reading:----")

    ValueListClean =[]
    NullValues = []
    for row in ValueListRaw:
        ValueListClean.append((round(row[0],8), round(row[1],1)))
        if round(row[1],1) == 0:
            NullValues.append((round(row[0],8), abs(round(row[1],1))))
    #print("Number of NullValues found: " + str(len(NullValues)))

    #printValueList(NullValues)
    #print("----Done cleaning data & finding null values")

    divValue = []
    for i in range(len(NullValues)-1):
        divValue.append((NullValues[i+1][0]-NullValues[i][0],i))
    #printValueList(divValue)
    #print("----Done calculating diffrence between value points")

    sum = 0
    for numberPair in divValue:
        sum += numberPair[0]
    average = sum/nullValues

    #print("Average time = " + str(average))

    periodicTime = 2*average

    #print("The periodic time is: " , periodicTime)
    return periodicTime


rawData1 = 'Exp1.csv'
rawData2 = 'Exp2.csv'
rawData3 = 'Exp3.csv'

firstAverage = calculatePeriodicTime(rawData1, 30)
secondAverage = calculatePeriodicTime(rawData2, 31)
thirdAverage = calculatePeriodicTime(rawData3,31)
totalAverage = (firstAverage + secondAverage + thirdAverage)/3

print("----" + rawData1 + "----")
print("     periodic time = " + str(firstAverage) + 's')
print("-------------------------")

print("----" + rawData2 + "----")
print("     periodic time = " + str(secondAverage) + 's')
print("-------------------------")

print("----" + rawData3 + "----")
print("     periodic time = " + str(thirdAverage) + 's')
print("-------------------------")

print("----" + "Combined Data" + "----")
print("     periodic time = " + str(totalAverage) + 's')
print("-------------------------")




