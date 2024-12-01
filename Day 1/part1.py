import numpy as np
# Read input
leftList = []
rightList = []
with open('input.txt', 'r') as file:
    for line in file:
        left, right = line.split()
        leftList.append(int(left))
        rightList.append(int(right))
# Print result
print(f"totalDistance = {np.sum(np.abs(np.array(sorted(rightList)) - np.array(sorted(leftList))))}")


# Part 2
simScore = 0
for i in range(len(leftList)):
    number = leftList[i]
    count = rightList.count(number)
    simScore += count*number
print(f"SimScore = {simScore}")
