import numpy as np

# Initialize containers
grid = []
commands = []

# Read the file
with open("input.txt") as file:
    lines = file.readlines()
    
    # Separate grid and commands dynamically
    separator_found = False
    for line in lines:
        if line.strip() == "":  # Empty line indicates the separator
            separator_found = True
            continue
        if not separator_found:
            grid.append(list(line.strip()))  # Add grid lines
        else:
            commands.extend(line.strip())  # Extend commands with characters

# Convert the grid to a NumPy array
grid_array = np.array(grid)



def update_map(Map, Command):
    iRobot, jRobot = np.where(Map == '@')
    # Find the first dot
    def update_coords(i,j,direction):
        if direction == 'v':
            return i+1, j
        if direction == '<':
            return i, j-1
        if direction == '^':
            return i-1, j
        if direction == '>':
            return i, j+1
        
        return 'error', 'error'

    dotFound = False
    boxFound = False
    i, j = iRobot, jRobot
    #print("c")
    #print(i,j)
    #print("start")
    while not dotFound:
        i, j = update_coords(i, j, Command)
        #print(Map[i,j][0])
        #print(i,j)
        if Map[i,j][0] == '#':
            #print(i,j)
            #print("broken")
            break
        if Map[i,j][0] == 'O':
            boxFound = True
            continue
        if Map[i,j][0] == ".":
            dotFound = True
    
    if dotFound:
        # Essentially shift everything found before finding the dot
        # Determine the direction of the shift
        iRobotNew, jRobotNew = update_coords(iRobot, jRobot, Command)
        Map[iRobotNew, jRobotNew] = '@'
        Map[iRobot, jRobot] = '.'
        if boxFound:
            Map[i,j] = 'O'

    return Map

for command in commands:
    grid_array = update_map(grid_array, command)

# Find sum of all gps coordinates
boxCoordinates = np.where(grid_array == 'O')

totalSum = 0
for i in range(len(boxCoordinates[0])):
    totalSum += 100*boxCoordinates[0][i] + boxCoordinates[1][i]
print(totalSum)