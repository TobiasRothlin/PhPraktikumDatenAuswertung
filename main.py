import csv

def printValueList(valList):
    print("lenght -> " + str(len(valList)))
    for line in valList:
        print(str(line[0]) + "\t\t\t\t |" + str(line[1]))
    return


with open('Exp1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='\n')
    ValueListRaw = []
    for row in spamreader:
        try:
            time = float(row[0])
            gyrY = float(row[2])
            ValueListRaw.append((time,gyrY))
        except:
            print("Not a number")

printValueList(ValueListRaw)
print("----Done file reading:----")

ValueListClean =[]
NullValues = []
for row in ValueListRaw:
    ValueListClean.append((round(row[0],8), round(row[1],1)))
    if round(row[1],1) == 0:
        NullValues.append((round(row[0],8), abs(round(row[1],1))))
print("Number of NullValues found: " + str(len(NullValues)))

printValueList(NullValues)
print("----Done cleaning data & finding null values")

divValue = []
for i in range(len(NullValues)-1):
    divValue.append((NullValues[i+1][0]-NullValues[i][0],i))
printValueList(divValue)






