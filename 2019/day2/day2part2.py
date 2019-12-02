import sys

with open('day2input.txt') as f:
    stringNumbers = f.read().split(',')

intNumbersOriginal = list(map(int, stringNumbers))
intNumberInUse = intNumbersOriginal

noun = 0
verb = 0

intNumberInUse[1] = noun
intNumberInUse[2] = verb

loop = True
operationPlace = 0

while loop is True:
    if intNumberInUse[operationPlace] == 1:
        intNumberInUse[intNumberInUse[operationPlace + 3]] = intNumberInUse[intNumberInUse[operationPlace + 1]] + intNumberInUse[intNumberInUse[operationPlace + 2]]
    elif intNumberInUse[operationPlace] == 2:
        intNumberInUse[intNumberInUse[operationPlace + 3]] = intNumberInUse[intNumberInUse[operationPlace + 1]] * intNumberInUse[intNumberInUse[operationPlace + 2]]
    elif intNumberInUse[operationPlace] == 99:
        if intNumberInUse[0] == 19690720:
            print("Noun is: " + str(noun))
            print("Verb is: " + str(verb))
            word = 100*noun + verb
            print("Result is: " + str(word))
            loop = False
        else:
            if noun < 99:
                noun = noun + 1
            else:
                noun = 0
                verb = verb + 1
                print("Noun reset, verb increased")
            
            intNumberInUse = list(map(int, stringNumbers))
            intNumberInUse[1] = noun
            intNumberInUse[2] = verb
            operationPlace = 0

        #print("Final result is: " + str(intNumberInUse[0]))
    else:
        print("Something went horribly wrong")
    operationPlace = operationPlace + 4

    #print(operationPlace)