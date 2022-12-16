# COMMAND SHIFT C OP
from collections import defaultdict
def towards(a, b):
    if a < b:
        a += 1 
    elif a > b:
        a -= 1
    return a
def findSandSpot(grid, sand_floor, coords=(500, 0)):
    #print (coords)
    if coords[1]+1 == sand_floor:
        return (coords[0], coords[1])
    if grid[(coords[0],coords[1]+1)] == 1:
        if grid[(coords[0]-1,coords[1]+1)] == 1:
            if grid[(coords[0]+1,coords[1]+1)] == 1:
                return (coords[0], coords[1])
            else:
                return findSandSpot(grid, sand_floor, (coords[0]+1, coords[1]+1))
        else:
            return findSandSpot(grid, sand_floor, (coords[0]-1, coords[1]+1))
    else:
        return findSandSpot(grid, sand_floor, (coords[0], coords[1]+1))

with open("inp14.txt") as f:
    c = [[[int(k) for k in j.strip().split(",")] for j in i.split("->")] for i in f.readlines()]
    #print (c)
    grid = defaultdict(lambda: 0)
    for i in c:
        # set the starting point
        grid[(i[0][0], i[0][1])] = 1
        for j in range(len(i)-1):
            if i[j][0] == i[j+1][0]:
                a = i[j][1]
                b = i[j+1][1]
                while a != b:
                    a = towards(a, b)
                    grid[(i[j][0], a)] = 1
            if i[j][1] == i[j+1][1]:
                a = i[j][0]
                b = i[j+1][0]
                while a != b:
                    a = towards(a, b)
                    grid[(a, i[j][1])] = 1
    sand_floor = (max([i[1] for i in grid]))+2
    sand = 0
    coords = findSandSpot(grid, sand_floor)
    while grid[(500, 0)] != 1:
        grid[(coords[0],coords[1])] = 1
        sand += 1
        coords = findSandSpot(grid, sand_floor)
    print (sand)

