import re
pattern = r"""
    Button\sA:\sX\+(\d+),\sY\+(\d+)\n     # Button A: X and Y offsets
    Button\sB:\sX\+(\d+),\sY\+(\d+)\n     # Button B: X and Y offsets
    Prize:\sX=(\d+),\sY=(\d+)             # Prize: X and Y positions
    """
with open('input.txt') as file:
    data = file.read()

matches = re.findall(pattern, data, re.VERBOSE)
machines = []
for match in matches:
    machines.append({
        "A": {"X": int(match[0]), "Y": int(match[1])},
        "B": {"X": int(match[2]), "Y": int(match[3])},
        "P": {"X": int(match[4]), "Y": int(match[5])},
    })

part2 = True
totalCost = 0
for m in machines:
    if part2:
        m['P']['X'] += 10000000000000
        m['P']['Y'] += 10000000000000

    # pen and paper    
    A = m['B']['Y'] * m['P']['X'] - m['B']['X'] * m['P']['Y']
    B = -m['A']['Y'] * m['P']['X'] + m['A']['X'] * m['P']['Y']
    denominator = m['A']['X']*m['B']['Y'] - m['B']['X']*m['A']['Y']
    A = A / denominator
    B = B / denominator
    
    if A == int(A) and B == int(B): # Whole number solution expected
        totalCost += A*3 + B
print(totalCost)