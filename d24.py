import time

with open("inp24.txt") as f:
    c = [i.strip() for i in f.readlines()]

def printBoard(b):
    for i in range(len(c)):
        s = ""
        for j in range(len(c[i])):
            if c[i][j] == "#":
                s += "#"
            else:
                if len(b[(i, j)]) > 1:
                    s += str(len(b[(i, j)]))
                elif len(b[(i, j)]) == 1:
                    s += b[(i, j)][0] 
                else:
                    s += "."
        print (s)
                

board = {}
for i in range(len(c)):
    for j in range(len(c[i])):
        if c[i][j] != ".":
            if c[i][j] in ["S", "E", "#"]:
                board[(i, j)] = ["#"]
            else:
                board[(i, j)] = [c[i][j]]
        else:
            board[(i, j)] = []
        
valid_squares = [(0, 1)]

round = 1

while (26, 120) not in valid_squares:
    print (round)
    # set up the new board
    newboard = {}
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] in ["S", "E", "#"]:
                newboard[(i, j)] = [c[i][j]]
            else:
                newboard[(i, j)] = []
    # shift all the arrows from the old board
    for i in range(len(c)):
        for j in range(len(c[i])):
            for k in board[(i, j)]:
                if k in ["S", "E", "#"]:
                    continue
                elif k == ">":
                    if c[i][j+1] in ["S", "E", "#"]:
                        newboard[(i, 1)].append(">")
                    else:
                        newboard[(i, j+1)].append(">")
                elif k == "<":
                    if c[i][j-1] in ["S", "E", "#"]:
                        newboard[(i, len(c[i])-2)].append("<")
                    else:
                        newboard[(i, j-1)].append("<")
                elif k == "^":
                    if c[i-1][j] in ["S", "E", "#"]:
                        newboard[(len(c)-2, j)].append("^")
                    else:
                        newboard[(i-1, j)].append("^")
                elif k == "v":
                    if c[i+1][j] in ["S", "E", "#"]:
                        newboard[(1, j)].append("v")
                    else:
                        newboard[(i+1, j)].append("v")
    # check the set of valid squares
    new_valid_squares = set([])
    for i in valid_squares:
        for j in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
            if (i[0]+j[0], i[1]+j[1]) in newboard and newboard[(i[0]+j[0], i[1]+j[1])] in [["S"], ["E"], []]:
                new_valid_squares.add((i[0]+j[0], i[1]+j[1]))
    valid_squares = list(new_valid_squares)
    board = newboard
    round += 1

valid_squares = [(26, 120)]

while (0, 1) not in valid_squares:
    print (round)
    # set up the new board
    newboard = {}
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] in ["S", "E", "#"]:
                newboard[(i, j)] = [c[i][j]]
            else:
                newboard[(i, j)] = []
    # shift all the arrows from the old board
    for i in range(len(c)):
        for j in range(len(c[i])):
            for k in board[(i, j)]:
                if k in ["S", "E", "#"]:
                    continue
                elif k == ">":
                    if c[i][j+1] in ["S", "E", "#"]:
                        newboard[(i, 1)].append(">")
                    else:
                        newboard[(i, j+1)].append(">")
                elif k == "<":
                    if c[i][j-1] in ["S", "E", "#"]:
                        newboard[(i, len(c[i])-2)].append("<")
                    else:
                        newboard[(i, j-1)].append("<")
                elif k == "^":
                    if c[i-1][j] in ["S", "E", "#"]:
                        newboard[(len(c)-2, j)].append("^")
                    else:
                        newboard[(i-1, j)].append("^")
                elif k == "v":
                    if c[i+1][j] in ["S", "E", "#"]:
                        newboard[(1, j)].append("v")
                    else:
                        newboard[(i+1, j)].append("v")
    # check the set of valid squares
    new_valid_squares = set([])
    for i in valid_squares:
        for j in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
            if (i[0]+j[0], i[1]+j[1]) in newboard and newboard[(i[0]+j[0], i[1]+j[1])] in [["S"], ["E"], []]:
                new_valid_squares.add((i[0]+j[0], i[1]+j[1]))
    valid_squares = list(new_valid_squares)
    board = newboard
    round += 1

valid_squares = [(0, 1)]

while (26, 120) not in valid_squares:
    print (round)
    # set up the new board
    newboard = {}
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] in ["S", "E", "#"]:
                newboard[(i, j)] = [c[i][j]]
            else:
                newboard[(i, j)] = []
    # shift all the arrows from the old board
    for i in range(len(c)):
        for j in range(len(c[i])):
            for k in board[(i, j)]:
                if k in ["S", "E", "#"]:
                    continue
                elif k == ">":
                    if c[i][j+1] in ["S", "E", "#"]:
                        newboard[(i, 1)].append(">")
                    else:
                        newboard[(i, j+1)].append(">")
                elif k == "<":
                    if c[i][j-1] in ["S", "E", "#"]:
                        newboard[(i, len(c[i])-2)].append("<")
                    else:
                        newboard[(i, j-1)].append("<")
                elif k == "^":
                    if c[i-1][j] in ["S", "E", "#"]:
                        newboard[(len(c)-2, j)].append("^")
                    else:
                        newboard[(i-1, j)].append("^")
                elif k == "v":
                    if c[i+1][j] in ["S", "E", "#"]:
                        newboard[(1, j)].append("v")
                    else:
                        newboard[(i+1, j)].append("v")
    # check the set of valid squares
    new_valid_squares = set([])
    for i in valid_squares:
        for j in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
            if (i[0]+j[0], i[1]+j[1]) in newboard and newboard[(i[0]+j[0], i[1]+j[1])] in [["S"], ["E"], []]:
                new_valid_squares.add((i[0]+j[0], i[1]+j[1]))
    valid_squares = list(new_valid_squares)
    board = newboard
    round += 1
