import sys

with open('day2input.txt') as f:
    stringNumbers = f.read().split(',')

intNumbers = list(map(int, stringNumbers))

intNumbers[1] = 12
intNumbers[2] = 2

loop = True
operationPlace = 0

#print(intNumbers[intNumbers[operationPlace + 3]])

while loop is True:
    if intNumbers[operationPlace] == 1:
        intNumbers[intNumbers[operationPlace + 3]] = intNumbers[intNumbers[operationPlace + 1]] + intNumbers[intNumbers[operationPlace + 2]]
    elif intNumbers[operationPlace] == 2:
        intNumbers[intNumbers[operationPlace + 3]] = intNumbers[intNumbers[operationPlace + 1]] * intNumbers[intNumbers[operationPlace + 2]]
    elif intNumbers[operationPlace] == 99:
        loop = False
        print("Final result is: " + str(intNumbers[0]))
    else:
        print("Something went horribly wrong")
    operationPlace = operationPlace + 4

    #print(operationPlace)