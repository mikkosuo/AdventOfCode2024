
inputData = []
with open('input.txt') as file:
    for line in file:
        key, values = line.strip().split(':')
        inputData.append((key.strip(), list(map(int, values.strip().split()))))

# Part 1
def is_valid_equation(Result, Terms):
    # DFS all possibilities
    def recursion(Result, NumOfTerms, CurrentResult, CurrentNumOfTerms, AllTerms):
        if CurrentNumOfTerms == NumOfTerms:
            if CurrentResult == Result:
                return True
            else:
                return False
        for i in range(2):
            if i == 0:
                returnVal = recursion(Result, NumOfTerms, CurrentResult * AllTerms[CurrentNumOfTerms],CurrentNumOfTerms+1, AllTerms)
            else:
                returnVal = recursion(Result, NumOfTerms, CurrentResult + AllTerms[CurrentNumOfTerms],CurrentNumOfTerms+1, AllTerms)
            if returnVal == True:
                return True
    return recursion(Result, len(Terms), Terms[0],1,Terms)
totalSum = 0
for entry in inputData:
    if is_valid_equation(int(entry[0]), entry[1]):
        totalSum += int(entry[0])
print(totalSum)


# Part 2
def is_valid_equation2(Result, Terms):
    # DFS all possibilities
    def recursion(Result, NumOfTerms, CurrentResult, CurrentNumOfTerms, AllTerms):
        if CurrentNumOfTerms == NumOfTerms:
            if CurrentResult == Result:
                return True
            else:
                return False
        for i in range(3):
            if i == 0:
                returnVal = recursion(Result, NumOfTerms, CurrentResult * AllTerms[CurrentNumOfTerms],CurrentNumOfTerms+1, AllTerms)
            elif i == 2:
                returnVal = recursion(Result, NumOfTerms, CurrentResult + AllTerms[CurrentNumOfTerms],CurrentNumOfTerms+1, AllTerms)
            else:
                returnVal = recursion(Result, NumOfTerms, int(str(CurrentResult) + str(AllTerms[CurrentNumOfTerms])),CurrentNumOfTerms+1, AllTerms)
            if returnVal == True:
                return True
    return recursion(Result, len(Terms), Terms[0],1,Terms)

totalSum = 0
for entry in inputData:
    if is_valid_equation2(int(entry[0]), entry[1]):
        totalSum += int(entry[0])
print(totalSum)