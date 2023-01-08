import numpy as np

def n(l):
    return np.array(l)

class Face():
    def __init__(self,grid, facing):
        self.grid = grid
        self.facing = facing # based on the current direction, which face it would be facing

cube = [] 
cs = 50 # cube size

def printGivenFace(x):
    s = []
    print ("Cube face: {a}".format(a=x))
    for i in cube[x].grid:
        s.append(i)
    if pos[1] != cs-1:
        s[pos[0]] = s[pos[0]][:pos[1]]+str(facing)+s[pos[0]][(pos[1]+1):]
    else:
        s[pos[0]] = s[pos[0]][:pos[1]]+str(facing)
    for i in s:
        print (i)

def printFace():
    s = []
    print ("Cube face: {a}".format(a=face_index))
    for i in cube[face_index].grid:
        s.append(i)
    if pos[1] != cs-1:
        s[pos[0]] = s[pos[0]][:pos[1]]+str(facing)+s[pos[0]][(pos[1]+1):]
    else:
        s[pos[0]] = s[pos[0]][:pos[1]]+str(facing)
    for i in s:
        print (i)

def printPosition():
    print ("position: {a}, face: {b}, facing: {c}".format(a=pos, b=face_index, c=facing))

def move():
    global face_index 
    global facing
    newpos = pos+offsets[facing]
    if 0 <= newpos[0] <= cs-1 and 0 <= newpos[1] <= cs-1:
        if cube[face_index].grid[newpos[0]][newpos[1]] == ".": 
            return newpos
        else:
            return -1
    # it must be off grid!
    #on the face that's [facing] away 
    new_face_index = cube[face_index].facing[facing]
    new_face = cube[new_face_index]
    #consider which side it will end up on 
    if (new_face_index, face_index) in [(1, 3), (2, 3), (3, 4), (4, 6), (5, 6), (6, 1)]:
        side = "D"
    if (new_face_index, face_index) in [(1, 6), (2, 6), (3, 2), (4, 3), (5, 3), (6, 5)]:
        side = "U"
    if (new_face_index, face_index) in [(1, 2), (2, 5), (3, 5), (4, 5), (5, 2), (6, 2)]:
        side = "L"
    if (new_face_index, face_index) in [(1, 4), (2, 1), (3, 1), (4, 1), (5, 4), (6, 4)]:
        side = "R"
    print (newpos)
    if newpos[0] < 0:
        offset = newpos[1]
    if newpos[1] < 0:
        offset = (cs-1)-newpos[0]
    if newpos[0] > (cs-1):
        offset = (cs-1)-newpos[1]
    if newpos[1] > (cs-1):
        offset = newpos[0]
    #consider the new facing as a result
    #find the new space and return new facing
    print (side)
    if side == "D": # it will be on the downside, so y is 49
        newpos = n([(cs-1), offset])
    if side == "U": 
        newpos = n([0, cs-1-offset])
    if side == "L": 
        newpos = n([offset, 0])
    if side == "R": 
        newpos = n([cs-1-offset, (cs-1)])
    if cube[new_face_index].grid[newpos[0]][newpos[1]] == ".":
        if side == "D": # it will be on the downside, so y is 49
            facing = 3
        if side == "U": 
            facing = 1
        if side == "L": 
            facing = 0
        if side == "R": 
            facing = 2
        face_index = new_face_index
        return newpos
    else:
        return -1

    #the issue is of course when that's a freaking wall but we'll get to that later

with open("inp22.txt") as f:
    c = [i.strip("\n") for i in f.readlines()]
    board = c[:len(c)-2]
    commands = c[len(c)-1]
    directions = []
    for i in commands:
        if i == "L" or i == "R":
            directions.append(i)
    movements = [int(i) for i in commands.replace("R", "L").split("L")]

offsets = {0: n([0, 1]), 1: n([1, 0]), 2: n([0, -1]), 3: n([-1, 0])}  

# six cubes

f1 = Face([i[cs*2:cs*3] for i in board[:cs]], [4,3,2,6])
f2 = Face([i[cs:cs*2] for i in board[:cs]], [1,3,5,6])
f3 = Face([i[cs:cs*2] for i in board[cs:cs*2]],[1,4,5,2])
f4 = Face([i[cs:cs*2] for i in board[cs*2:cs*3]],[1,6,5,3])
f5 = Face([i[:cs] for i in board[cs*2:cs*3]],[4,6,2,3])
f6 = Face([i[:cs] for i in board[cs*3:cs*4]],[4,1,2,5])
cube = [0, f1, f2, f3, f4, f5, f6] # 0 is a placeholder for 1-indexing

for i in range(len(f1.grid[0])):
    if f1.grid[0][i] == ".":
        validx = i
        break

pos = n([0, validx]) # leftmost valid x position
face_index = 2
facing = 0

#printFace()
#printPosition()
#pos = move()
#printFace()
#printPosition()
for index, i in enumerate(movements):
    #print (i)
    # do the thing i times
    for j in range(i):
        #printPosition()
        #printFace()
        c = move()
        if type(c) != int:
            pos = c
    if index < len(directions):
        if directions[index] == "R":
            facing += 1
        else:
            facing -= 1
        facing = facing % 4
printPosition()
printFace()
# manually calculate facing at the end

"""
    ........
    ........
    ........
    ........
    ....
    ....
    ....
    ....
........
........
........
........
....
....
....
....

1R20R1
"""