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

while True:
    # Remove trailing dots
    lastElem = sequence[-1]
    while lastElem == '.':
        del sequence[-1]
        lastElem = sequence[-1] 
    if '.' not in sequence:
        break
    dotIndex = sequence.index('.')
    sequence[dotIndex] = sequence[-1]
    # Remove last elem
    del sequence[-1]

# Calculcate checksum
sum = 0 
for i in range(len(sequence)):
    sum += i*sequence[i]
print(sum)

