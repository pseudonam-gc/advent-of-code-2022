import time
import math
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
        if grid[i] != ["." for i in range(7)]:
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
starter = 20000
distance = 1000
for piece in range(int(1e10)):
    # check for cycles up to the length of half the grid
    succ = 0
    h = height(grid)
    if piece == starter-1:
        # record the height
        recorded_height = h
    elif piece > starter+10: # some arbitrary constant to prevent the same thing from being chosen
        if grid[(h-distance):h] == grid[(recorded_height-distance):recorded_height]:
            piecedif = piece - starter
            heightdif = h-recorded_height
            succ = 1
            break
    if succ == 1:
        break
    addshape(shapes[piece % 5])
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
    locs = []

#piecedif -= 1
stacks = math.floor((1000000000000-piece-distance)/piecedif)
print ("heightdif:"+str(heightdif))
print ("piecedif:"+str(piecedif))
print ("piece:"+str(piece))
print ("stacks:"+str(stacks))
rem_pieces = 1000000000000-piece-piecedif*stacks
h = heightdif*stacks
print ("h"+str(height(grid)))
print (height(grid)+1+h)
print ("remaining pieces:"+str(rem_pieces))

# optimal is 1514285714288

for i in range(piece, rem_pieces+piece):
    addshape(shapes[i % 5])
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
    locs = []

true_height = (height(grid)+1)+h
print (true_height)

# 1578107183540 too high
# will guess 1577207977186

# THIS CODE WAS WRITTEN BY SCHRODINGER'S CAT