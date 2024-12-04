InputMatrix = []
with open('input.txt') as file:
    for line in file:
        InputMatrix.append(line.strip('\n'))


def check_connections(InputMatrix, i, j):
    found = 0
    # Left
    if j > 2:
        if ['M','A','S'] == [InputMatrix[i][j-1], InputMatrix[i][j-2], InputMatrix[i][j-3]]:
             found += 1
    # Right
    if j < len(InputMatrix[j]) - 3:
        if ['M','A','S'] == [InputMatrix[i][j+1], InputMatrix[i][j+2], InputMatrix[i][j+3]]:
             found += 1
    # Up
    if i > 2:
        if ['M','A','S'] == [InputMatrix[i-1][j], InputMatrix[i-2][j], InputMatrix[i-3][j]]:
             found += 1
    # Down
    if i < len(InputMatrix) - 3:
        if ['M','A','S'] == [InputMatrix[i+1][j], InputMatrix[i+2][j], InputMatrix[i+3][j]]:
             found += 1
    # Diagonal up left
    if j > 2 and i > 2:
        if ['M','A','S'] == [InputMatrix[i-1][j-1], InputMatrix[i-2][j-2], InputMatrix[i-3][j-3]]:
             found += 1
    # Diagonal up right
    if j < len(InputMatrix[j]) - 3 and i > 2:
        if ['M','A','S'] == [InputMatrix[i-1][j+1], InputMatrix[i-2][j+2], InputMatrix[i-3][j+3]]:
             found += 1
    # Diagonal down left
    if j > 2 and i < len(InputMatrix) - 3:
        if ['M','A','S'] == [InputMatrix[i+1][j-1], InputMatrix[i+2][j-2], InputMatrix[i+3][j-3]]:
             found += 1
    # Diagonal down right
    if j < len(InputMatrix[j]) - 3 and i < len(InputMatrix) - 3:
        if ['M','A','S'] == [InputMatrix[i+1][j+1], InputMatrix[i+2][j+2], InputMatrix[i+3][j+3]]:
             found += 1
    return found

# Part 1
found = 0
for i in range(len(InputMatrix)):
    for j in range(len(InputMatrix[i])):
        if InputMatrix[i][j] == 'X':
                found += check_connections(InputMatrix, i, j)

print(f"Part 1 found {found}")



def check_connections_2(InputMatrix, i, j):
    found = 0

    if not (j > 0 and i > 0 and j < len(InputMatrix[j]) - 1 and i < len(InputMatrix) - 1):
        return False
    
    if ['M', 'S'] == [InputMatrix[i-1][j-1], InputMatrix[i+1][j+1]]:
        found += 1
    if ['M', 'S'] == [InputMatrix[i+1][j+1], InputMatrix[i-1][j-1]]:
         found += 1
    if ['M', 'S'] == [InputMatrix[i+1][j-1], InputMatrix[i-1][j+1]]:
        found += 1
    if ['M', 'S'] == [InputMatrix[i-1][j+1], InputMatrix[i+1][j-1]]:
        found += 1

    return True if found > 1 else False

# Part 2
found = 0
for i in range(len(InputMatrix)):
    for j in range(len(InputMatrix[i])):
        if InputMatrix[i][j] == 'A':
                found += check_connections_2(InputMatrix, i, j)

print(f"Part 2 found {found}")