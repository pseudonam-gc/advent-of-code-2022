import math
import numpy as np
with open("inp9.txt") as f:
    c = [(i.strip().split()[0], int(i.strip().split()[1])) for i in f.readlines()]
    print (c)
l = []
for i in c:
    for j in range(i[1]):
        l.append(i[0])

positions = set()
knots = []
for i in range(10):
    knots.append([0, 0])

positions.add((0, 0))

for i in l:
    if i == "L":
        knots[0][0] -= 1
    if i == "R":
        knots[0][0] += 1
    if i == "U":
        knots[0][1] += 1
    if i == "D":
        knots[0][1] -= 1
    for j in range(9):
        distance = sum([(i-j)**2 for i, j in zip(knots[j], knots[j+1])])
        if distance > 2:
            if knots[j][0] == knots[j+1][0]:
                if knots[j][1] + 2 == knots[j+1][1]:
                    knots[j+1][1] -= 1
                elif knots[j][1] - 2 == knots[j+1][1]:
                    knots[j+1][1] += 1
            elif knots[j][1] == knots[j+1][1]:
                if knots[j][0] + 2 == knots[j+1][0]:
                    knots[j+1][0] -= 1
                elif knots[j][0] - 2 == knots[j+1][0]:
                    knots[j+1][0] += 1
            else:
                if knots[j][0] > knots[j+1][0] and knots[j][1] > knots[j+1][1]:
                    knots[j+1][0] += 1 
                    knots[j+1][1] += 1
                elif knots[j][0] > knots[j+1][0] and knots[j][1] < knots[j+1][1]:
                    knots[j+1][0] += 1 
                    knots[j+1][1] -= 1
                elif knots[j][0] < knots[j+1][0] and knots[j][1] < knots[j+1][1]:
                    knots[j+1][0] -= 1 
                    knots[j+1][1] -= 1
                elif knots[j][0] < knots[j+1][0] and knots[j][1] > knots[j+1][1]:
                    knots[j+1][0] -= 1 
                    knots[j+1][1] += 1
    positions.add(tuple(knots[9]))
print (len(positions))
#print (positions)