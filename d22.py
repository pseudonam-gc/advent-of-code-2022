import numpy as np
with open("inp22.txt") as f:
    c = [i.strip("\n") for i in f.readlines()]
    board = []
    board = c[:len(c)-2]
    commands = c[len(c)-1]
    directions = []
    for i in commands:
        if i == "L" or i == "R":
            directions.append(i)
    movements = [int(i) for i in commands.replace("R", "L").split("L")]

offsets = {0: np.array([0, 1]), 1: np.array([-1, 0]), 2: np.array([0, -1]), 3: np.array([1, 0])} 

facing = 0 # 0 = right and then just use +1 -1 
for i in range(len(board[0])):
    if board[0][i] == ".":
        validx = i
        break
pos = np.array([0, validx]) # should be the leftmost valid x position, i think

def ongrid(pos):
    if 0 <= pos[0] <= len(board)-1 and 0 <= pos[1] <= len(board[pos[0]])-1:
        return True 
    return False

def validmove(pos, facing):
    newpos = pos+offsets[facing]
    if ongrid(newpos) == False or board[newpos[0]][newpos[1]] == " ": 
        # then keep going in the OPPOSITE of the facing direction until a " " is found; stop right before it
        newpos = newpos-offsets[facing]
        while ongrid(newpos) == True and board[newpos[0]][newpos[1]] != " ":
            newpos = newpos-offsets[facing]
        newpos = newpos+offsets[facing]
        # lmao this do while workaround is freaking hilarious
        if board[newpos[0]][newpos[1]] == "#" or ongrid(newpos) == False:
            # whoops we hit a fricking wall
            return -1
        return newpos
    elif board[newpos[0]][newpos[1]] == "#": 
        return -1
    else: 
        return newpos
        # it is valid

for index, i in enumerate(movements):
    #print (i)
    # do the thing i times
    for j in range(i):
        c = validmove(pos, facing)
        if type(c) != int:
            pos = c
        #print (pos, facing)
    if index < len(directions):
        if directions[index] == "R":
            facing -= 1
        else:
            facing += 1
        facing = facing % 4

print ((pos[0]+1)*1000+(pos[1]+1)*4)
print (facing)