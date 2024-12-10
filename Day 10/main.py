inputMap = []
with open('input.txt') as file:
    for line in file:
        inputMap.append([int(c) for c in line.strip()])

# Part 1 dont count same goal twice
class checked():
    def __init__(self):
        self._checked = set()
        self._part2 = True
    def reset(self):
        self._checked.clear()
    def add(self, E):
        self._checked.add(E)
    def is_counted(self, E):
        if self._part2:
            return False
        return E in self._checked
cc = checked()


def dfs(InputMap, I, J, LastHeight, TotalScore):
    NewHeight = InputMap[I][J] 
    if NewHeight - 1 != LastHeight:
        return
    if InputMap[I][J] == 9:
        if not cc.is_counted((I,J)):
            TotalScore[0] += 1
        cc.add((I,J))
        return
    for i, j in [(I-1, J), (I+1, J), (I, J-1), (I, J+1)]:
            if i < 0 or i > len(inputMap)-1 or j < 0 or j > len(inputMap[i])-1:
                continue
            dfs(InputMap, i, j, NewHeight, TotalScore)
     
sumOfTheScores = 0
for i in range(len(inputMap)):
    for j in range(len(inputMap)):
        if inputMap[i][j] == 0:
            totalScore = [0]
            cc.reset()
            dfs(inputMap, i, j, -1, totalScore)
            sumOfTheScores += totalScore[0]

print(sumOfTheScores)