import re
# Read input text from file
with open('input.txt', 'r') as file:
    input_text = file.read()

# Regular expression to match the lines
pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

# Find all matches and convert them to dictionaries
matches = re.findall(pattern, input_text)
robots = [
    {"p": (int(p1), int(p2)), "v": (int(v1), int(v2))}
    for p1, p2, v1, v2 in matches
]


# Part 1
positions = []
width = 101
height = 103
for r in robots:
    newX = (r['p'][0]+100*r['v'][0]) % width
    newY = (r['p'][1]+100*r['v'][1]) % height
    positions.append((newX, newY))
safetyFactor = 1
quad1Sum = 0
quad2Sum = 0
quad3Sum = 0
quad4Sum = 0
quadWidth = (width-1)/2
quadHeight = (height-1)/2 
for pos in positions:
    if pos[0] < quadWidth and pos[1] < quadHeight:
        quad1Sum +=1 
    if pos[0] > quadWidth and pos[1] < quadHeight:
        quad2Sum +=1 
    if pos[0] < quadWidth and pos[1] > quadHeight:
        quad3Sum +=1 
    if pos[0] > quadWidth and pos[1] > quadHeight:
        quad4Sum +=1 
safetyFactor = quad1Sum * quad2Sum * quad3Sum * quad4Sum
print(safetyFactor)


import matplotlib.pyplot as plt
import numpy as np
# Part 2 print the frames one by one
def print_positions(Positions,t, AverageSafetyFactor):
    Matrix = np.zeros((height, width))
    for pos in Positions:
        Matrix[pos[1],pos[0]] = 1

    safetyFactor = 0
    quad1Sum = 0
    quad2Sum = 0
    quad3Sum = 0
    quad4Sum = 0
    print(t)
    for pos in positions:
        if pos[0] < quadWidth and pos[1] < quadHeight:
            quad1Sum +=1 
        if pos[0] > quadWidth and pos[1] < quadHeight:
            quad2Sum +=1 
        if pos[0] < quadWidth and pos[1] > quadHeight:
            quad3Sum +=1 
        if pos[0] > quadWidth and pos[1] > quadHeight:
            quad4Sum +=1 
        safetyFactor = quad1Sum * quad2Sum * quad3Sum * quad4Sum
    AverageSafetyFactor = (AverageSafetyFactor * t + safetyFactor) / (t+1)
    if safetyFactor < AverageSafetyFactor / 2:
        plt.title(t)
        plt.imshow(Matrix)
        plt.show()

    return AverageSafetyFactor

averageSafetyFactor = 0
for t in range(65000):
    positions = []
    width = 101
    height = 103    
    for r in robots:
        newX = (r['p'][0]+t*r['v'][0]) % width
        newY = (r['p'][1]+t*r['v'][1]) % height
        positions.append((newX, newY))
    averageSafetyFactor = print_positions(positions,t,averageSafetyFactor)
