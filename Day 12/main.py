garden = []
with open('input.txt') as file:
    for line in file:
        garden.append([char for char in line.strip()])

regions = []
for i in range(len(garden)):
    for j in range(len(garden)):
        # Check if this plant has neighbour in some region
        regionIndices = []
        for (i2, j2) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            if i2 < 0 or j2 < 0 or i2 == len(garden) or j2 == len(garden[i2]):
                    continue
            for iRegion, region in enumerate(regions):
                for key, val in region.items():
                    if (i2,j2) in val and key == garden[i][j]:
                        if iRegion not in regionIndices:
                            regionIndices.append(iRegion)
                
        if len(regionIndices) == 0:
            regions.append({garden[i][j] : [(i,j)]})
        elif len(regionIndices) == 1:
            regions[regionIndices[0]][garden[i][j]].append((i,j))
        else: # add to first and merge the rest to the first region
            regions[regionIndices[0]][garden[i][j]].append((i,j))
            for regIndex in sorted(regionIndices[1:], reverse=True):
                regions[regionIndices[0]][garden[i][j]] += regions[regIndex][garden[i][j]]
                del regions[regIndex]
            
# Part 1
totalCost = 0
for region in regions:
    plants = list(region.values())[0]
    # Count the fences
    numOfFences = 0
    for (i,j) in plants:
        for (i1, j1) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if (i1,j1) not in plants:
                numOfFences +=1
    totalCost += numOfFences * len(plants)
print(totalCost)



# Part 2
totalCost = 0
for region in regions:
    plants = list(region.values())[0]
    plantType = list(region.keys())[0]
    corners = 0
    
    plantExposed = {}  # For detecting outward corners
    plantExposers = {} # For detecting inward corners
    for (i,j) in plants:
        plantExposed[(i,j)] = []
        for dir, (i1, j1) in enumerate([(i+1,j), (i-1,j), (i,j+1), (i,j-1)]): # Down, Up, right, left
            if (i1,j1) not in plants:
                if (i1,j1) not in plantExposers.keys():
                    plantExposers[(i1,j1)] = []
                if dir == 0:
                    plantExposed[(i,j)].append("down")
                    plantExposers[(i1,j1)].append("up")
                elif dir == 1:
                    plantExposed[(i,j)].append("up")
                    plantExposers[(i1,j1)].append("down")
                elif dir == 2:
                    plantExposed[(i,j)].append("right")
                    plantExposers[(i1,j1)].append("left")
                elif dir == 3:
                    plantExposed[(i,j)].append("left")
                    plantExposers[(i1,j1)].append("right")
    
    topRight = 0
    topLeft = 0
    bottomLeft = 0
    bottomRight = 0
    for plant, dir in plantExposed.items():
        if "up" in dir and "right" in dir:
            topRight+=1
        if "up" in dir and "left" in dir:
            topLeft+=1
        if "down" in dir and "right" in dir:
            bottomRight+=1
        if "down" in dir and "left" in dir:
            bottomLeft+=1
    
    corners += topRight + topLeft + bottomLeft + bottomRight

    topRight = 0
    topLeft = 0
    bottomLeft = 0
    bottomRight = 0
    for differenPlant, dir in plantExposers.items():
        if "up" in dir and "right" in dir:
            if (differenPlant[0]-1, differenPlant[1]+1) in plants:
                topRight+=1
        if "up" in dir and "left" in dir:
            if (differenPlant[0]-1, differenPlant[1]-1) in plants:
                topLeft+=1
        if "down" in dir and "right" in dir:
            if (differenPlant[0]+1, differenPlant[1]+1) in plants:
                bottomRight+=1
        if "down" in dir and "left" in dir:
            if (differenPlant[0]+1, differenPlant[1]-1) in plants:
                bottomLeft+=1
    corners += topRight + topLeft + bottomLeft + bottomRight
    totalCost += corners * len(plants)
print(totalCost)


