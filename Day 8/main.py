import math

# Read data
numOfRows = 0
numOfColumns = 0
frequencyCoordinates = {}
with open('input.txt') as file:
    for i, line in enumerate(file):
        numOfRows += 1
        for j, c in enumerate(line.strip()):
            if i == 0:
                numOfColumns += 1
            if c != '.':
                if c in frequencyCoordinates.keys():
                    frequencyCoordinates[c].append((i,j))
                else:
                    frequencyCoordinates[c] = [(i,j)]

part2 = True
# Find antinodes
nodeLocations = set()
for frequency, coordinates in frequencyCoordinates.items():
    for coord1 in range(len(coordinates)):
        for coord2 in range(coord1+1, len(coordinates)):
            order = 0
            while True:
                out1 = False
                out2 = False
                if not part2:
                    iNode1 = (coordinates[coord1][0] + coordinates[coord1][0] - coordinates[coord2][0])
                    jNode1 = (coordinates[coord1][1] + coordinates[coord1][1] - coordinates[coord2][1])
                    iNode2 = (coordinates[coord1][0] + 2*(coordinates[coord2][0] - coordinates[coord1][0]))
                    jNode2 = (coordinates[coord1][1] + 2*(coordinates[coord2][1] - coordinates[coord1][1]))
                else:
                    iDir = coordinates[coord2][0] - coordinates[coord1][0]
                    jDir = coordinates[coord2][1] - coordinates[coord1][1]
                    gcd = math.gcd(iDir, jDir)
                    iNode1 = int(coordinates[coord1][0] + order*(iDir)/gcd)
                    jNode1 = int(coordinates[coord1][1] + order*(jDir)/gcd)
                    iNode2 = int(coordinates[coord1][0] - order*(iDir)/gcd)
                    jNode2 = int(coordinates[coord1][1] - order*(jDir)/gcd)
                if iNode1 >= 0 and iNode1 < numOfRows and jNode1 >= 0 and jNode1 < numOfColumns:
                    nodeLocations.add((iNode1, jNode1))
                else:
                    out1 = True
                if iNode2 >= 0 and iNode2 < numOfRows and jNode2 >= 0 and jNode2 < numOfColumns:
                    nodeLocations.add((iNode2, jNode2))
                else:
                    out2 = True
                if not part2 or (out1 and out2):
                    break
                order+=1

print(len(nodeLocations))

