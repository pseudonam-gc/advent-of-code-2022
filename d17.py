import time

with open("inp17.txt") as f:
    s = f.read().strip()

oldshapes = [
["..@@@@."], 
[
"...@...",
"..@@@..", 
"...@..."], 
[
"....@..",
"....@..", 
"..@@@.."], 
[
"..@....",
"..@....",
"..@....",
"..@...."], 
[
"..@@...",
"..@@..."]]
shapes = [[[k for k in j] for j in i] for i in oldshapes][:]
locs = []
grid = []
def printgrid():
    print ("GRID:")
    for i in range(len(grid)):
        print ("|"*(4-len(str(len(grid)-i-1)))+str(len(grid)-i-1)+"".join(grid[len(grid)-1-i]))

def height(grid):
    for i in range(len(grid)-1, 0, -1):
        if grid[i] != [i for i in "......."]:
            return i
    return 0

def addshape(shape):
    while height(grid)+3 > len(grid):
        grid.append([i for i in "......."])
    while height(grid)+4 < len(grid):
        grid.pop()
    for i in range(len(shape)):
        grid.append([i for i in shape[len(shape)-i-1]])
    ival = -1
    #printgrid()
    for i in range(len(grid)-1, -1, -1):
        if ival != -1 and i != ival: 
            break
        for j in range(7):
            if grid[i][j] == "@":
                ival = i-1
                locs.append([i, j])

def shapestop(direction): # determine if any # has a neighbor on the specified side (or is on the bottom of the grid)
    ival = -1 # once a @ is seen, this is used 
    for i in range(len(grid)-1, -1, -1):
        if ival != -1 and i != ival: 
            return False 
        if "@" in grid[i]: # check each row from newest to latest if it's a @ 
            ival = i-1
            for j in range(7):
                if grid[i][j] == "@":
                    if direction == "D":
                        if i == 0:
                            return True
                        elif grid[i-1][j] == "#":
                            return True
                    elif direction == "L":
                        if j == 0:
                            return True
                        elif grid[i][j-1] == "#":
                            return True
                    elif direction == "R":
                        if j == 6:
                            return True
                        elif grid[i][j+1] == "#":
                            return True
    return False

def fall(direction):
    newlocs = []
    for i in locs:
        if direction == "D":
            grid[i[0]-1][i[1]] = "@"
            newlocs.append([i[0]-1, i[1]])
        if direction == "R":
            grid[i[0]][i[1]+1] = "@"
            newlocs.append([i[0], i[1]+1])
        if direction == "L":
            grid[i[0]][i[1]-1] = "@"
            newlocs.append([i[0], i[1]-1])
    for i in locs:
        if i not in newlocs:
            grid[i[0]][i[1]] = "."
    return newlocs

def stop():
    ival = -1 # once a @ is seen, this is used 
    for i in range(len(grid)-1, -1, -1):
        if ival != -1 and i != ival: 
            return False 
        if "@" in grid[i]: # check each row from newest to latest if it's a @ 
            ival = i-1
            for j in range(7):
                if grid[i][j] == "@":
                    grid[i][j] = "#"

sindex = 0
for r in range(1000000000000):
    if r % 10000 == 0:
        print (r)
    addshape(shapes[r % 5])
    while True:  
        if s[sindex % len(s)] == "<":
            if shapestop("L") == False:
                locs = fall("L")
        else:
            if shapestop("R") == False:
                locs = fall("R")
        sindex += 1
        if shapestop("D") == False:
            locs = fall("D")
        else:
            break
    stop()  
    # check if the grid matches a hash; if so, yeeeeeeeet
    locs = []
print (height(grid)+1)