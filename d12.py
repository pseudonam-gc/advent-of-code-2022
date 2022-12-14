def validMoves(x, y, c):
    adjacentSquares = []
    validSquares = []
    if x > 0:
        adjacentSquares.append((x-1, y))
    if x < len(c[0])-1:
        adjacentSquares.append((x+1, y))
    if y > 0:
        adjacentSquares.append((x, y-1))
    if y < len(c)-1:
        adjacentSquares.append((x, y+1))
    for i in adjacentSquares:
        if c[i[1]][i[0]] == "E":
            if c[y][x] == "z" or c[y][x] == "y":
                validSquares.append((i[0], i[1]))
        elif c[y][x] == "S":
            if c[i[1]][i[0]] in ["a", "b"]:
                validSquares.append((i[0], i[1]))
        elif ord(c[i[1]][i[0]]) - ord("a") <= ord(c[y][x]) - ord("a") + 1:
            validSquares.append((i[0], i[1]))
    return validSquares
            
def printList(l):
    for i in l:
        print (i)
def printGrid(l):
    for i in l:
        print (" ".join([str(x) for x in i]))

with open("inp12.txt") as f:
    c = f.read().splitlines()
    floodfill = []
    for i in range(len(c)):
        floodfill.append([])
        for j in range(len(c[i])):
            if c[i][j] != "S" and c[i][j] != "a":
                floodfill[i].append(-1)
            else:
                floodfill[i].append(0)
    for n in range(0, 500):
        for i in range(len(c)):
            for j in range(len(c[i])):
                if floodfill[i][j] == n:
                    v = validMoves(j, i, c)
                    for k in v:
                        if floodfill[k[1]][k[0]] == -1:
                            floodfill[k[1]][k[0]] = n+1


    printGrid(floodfill)

for i in range(len(c)):
    for j in range(len(c[i])):
        if c[i][j] == "E":
            print (floodfill[i][j])