inputStr = ""
with open('input.txt') as file:
    for line in file:
        inputStr += line.strip()

sequence = []
id = 0
for i in range(0, int(len(inputStr)), 2):
    numOfBlocks = inputStr[i]
    for _ in range(int(numOfBlocks)):
        sequence.append(id)
    try:
        numOfFree = inputStr[i+1]
        for _ in range(int(numOfFree)):
            sequence.append('.')
    except IndexError as e:
        a = 1 # No free space after the last block
    id += 1



def find_slice(List, Query, IDIndex):
    for i in range(IDIndex):
        # Check if the slice matches the query
        if List[i:i + len(Query)] == Query:
            return i  # Return start index
    return None  # Return None if no match is found

alreadyMoved = set()
while True:    
    # Find the largest ID that hasn't been moved
    largestID = -1
    countOfLargestIDs = 0
    foundID = False
    for id in reversed(sequence):
        if foundID:
            if largestID == id:
                countOfLargestIDs+=1
            else:
                break

        if id != '.' and id not in alreadyMoved:
            largestID = id
            alreadyMoved.add(largestID)
            foundID = True
            countOfLargestIDs += 1
            continue
    
    if not foundID:
        break
    
    IDIndex = sequence.index(largestID)
    # Find a first free place that can fit these numbers
    dotIndex = find_slice(sequence, ['.' for _ in range(countOfLargestIDs)], IDIndex)
    if(dotIndex == None):
        continue

    # Move the whole files
    if foundID:
        for i in range(countOfLargestIDs):
            sequence[dotIndex+i] = sequence[IDIndex+i]
            sequence[IDIndex+i] = '.'

# Calculcate checksum
sum = 0 
for i in range(len(sequence)):
    if sequence[i] != '.':
        sum += i*sequence[i]
    else:
        continue
print(sum)