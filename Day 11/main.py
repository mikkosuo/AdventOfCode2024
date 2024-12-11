initialArrangment = []
with open("input.txt") as file:
    for line in file:
        for c in line.strip().split(' '):
            initialArrangment.append(int(c))
print(f"Initial arrangement: {initialArrangment}")

def blink(Arrangment):
    newArrangment = []
    for stone in Arrangment:
        if stone == 0:
            newArrangment.append(1)
        elif len(str(stone)) % 2 == 0:
            length = int(len(str(stone)))
            half1 = int(str(stone)[0:int(length/2)])
            half2 = int(str(stone)[int(length/2):int(length)])
            newArrangment.append(half1)
            newArrangment.append(half2)
        else:
            newArrangment.append(stone*2024)
    return newArrangment

# Part 1
list1 = initialArrangment
for _ in range(25):
    list1 = blink(list1)
print(len(list1))




# Part 2 when in doubt hashmap or something
def blink2(MapOfStones):
    newMapOfStones = {}
    for stone, count in MapOfStones.items():
        # Check what this stone will become
        newStones = blink([stone])

        # Add the counts to the new map of stgones
        for stone in newStones:
            if stone not in newMapOfStones:
                newMapOfStones[stone] = count
            else:
                newMapOfStones[stone] += count
    return newMapOfStones

mapOfStones = {}
for stone in initialArrangment:
    if stone in mapOfStones.keys():
        mapOfStones[stone] += 1
    else:
        mapOfStones[stone] = 1

print(f"Initial map of stones {mapOfStones}")
for _ in range(75):
    mapOfStones = blink2(mapOfStones)

totalCount = 0
for count in mapOfStones.values():
    totalCount+=count
print(totalCount)