from collections import defaultdict

with open("inp23.txt") as f:
    c = [i.strip() for i in f.readlines()]

loc = defaultdict(lambda: 0) # map of ordered (i, j) tuples or something idk

def displayDict(d):
    s = []
    for i in range(14):
        s.append("")
        for j in range(14):
            if d[(i, j)] != 0:
                s[i]+="#"
            else:
                s[i]+="."
                d.pop((i, j))
    for i in s:
        print (i)

def neighbors(pos): 
    n = []
    adjacent = [(0, 1),(1, 0),(0, -1),(-1, 0),(1, 1), (-1, -1), (-1, 1), (1, -1)]
    for i in adjacent:
        newpos = (pos[0]+i[0], pos[1]+i[1])
        if newpos in loc:
            n.append(i)
    return n

for i in range(len(c)):
    for j in range(len(c[i])):
        if c[i][j] == "#":
            loc[(i,j)] = 1

for round in range(1, 10000):

    proposal = defaultdict(lambda: 0)

    for i in loc.items():
        # proposal phase
        key = i[0]
        n = neighbors(key)
        # the order is north south west east
        if n == []:
            continue
        if round % 4 == 1:
            if (-1, 0) not in n and (-1, -1) not in n and (-1, 1) not in n:
                proposal[(key[0]-1, key[1])] += 1
                loc[key] = (key[0]-1, key[1])
            elif (1, 0) not in n and (1, 1) not in n and (1, -1) not in n:
                proposal[(key[0]+1, key[1])] += 1
                loc[key] = (key[0]+1, key[1])
            elif (0, -1) not in n and (1, -1) not in n and (-1, -1) not in n:
                proposal[(key[0], key[1]-1)] += 1
                loc[key] = (key[0], key[1]-1)
            elif (0, 1) not in n and (1, 1) not in n and (-1, 1) not in n:
                proposal[(key[0], key[1]+1)] += 1
                loc[key] = (key[0], key[1]+1)
        elif round % 4 == 2:
            if (1, 0) not in n and (1, 1) not in n and (1, -1) not in n:
                proposal[(key[0]+1, key[1])] += 1
                loc[key] = (key[0]+1, key[1])
            elif (0, -1) not in n and (1, -1) not in n and (-1, -1) not in n:
                proposal[(key[0], key[1]-1)] += 1
                loc[key] = (key[0], key[1]-1)
            elif (0, 1) not in n and (1, 1) not in n and (-1, 1) not in n:
                proposal[(key[0], key[1]+1)] += 1
                loc[key] = (key[0], key[1]+1)
            elif (-1, 0) not in n and (-1, -1) not in n and (-1, 1) not in n:
                proposal[(key[0]-1, key[1])] += 1
                loc[key] = (key[0]-1, key[1])
        elif round % 4 == 3:
            if (0, -1) not in n and (1, -1) not in n and (-1, -1) not in n:
                proposal[(key[0], key[1]-1)] += 1
                loc[key] = (key[0], key[1]-1)
            elif (0, 1) not in n and (1, 1) not in n and (-1, 1) not in n:
                proposal[(key[0], key[1]+1)] += 1
                loc[key] = (key[0], key[1]+1)
            elif (-1, 0) not in n and (-1, -1) not in n and (-1, 1) not in n:
                proposal[(key[0]-1, key[1])] += 1
                loc[key] = (key[0]-1, key[1])
            elif (1, 0) not in n and (1, 1) not in n and (1, -1) not in n:
                proposal[(key[0]+1, key[1])] += 1
                loc[key] = (key[0]+1, key[1])
        elif round % 4 == 0:
            if (0, 1) not in n and (1, 1) not in n and (-1, 1) not in n:
                proposal[(key[0], key[1]+1)] += 1
                loc[key] = (key[0], key[1]+1)
            elif (-1, 0) not in n and (-1, -1) not in n and (-1, 1) not in n:
                proposal[(key[0]-1, key[1])] += 1
                loc[key] = (key[0]-1, key[1])
            elif (1, 0) not in n and (1, 1) not in n and (1, -1) not in n:
                proposal[(key[0]+1, key[1])] += 1
                loc[key] = (key[0]+1, key[1])
            elif (0, -1) not in n and (1, -1) not in n and (-1, -1) not in n:
                proposal[(key[0], key[1]-1)] += 1
                loc[key] = (key[0], key[1]-1)

    newloc = defaultdict(lambda: 0)
    for i in loc.items():
        key = i[0]
        proposed_space = loc[key] 
        if proposed_space == 0:
            # if the elf didn't propose anything
            newloc[key] = 1
        if proposal[proposed_space] == 1:
            # then move there 
            newloc[proposed_space] = 1
        else:
            # just keep the same space
            newloc[key] = 1
    #print (round)
    if loc == newloc:
        print (round)
        break
    loc = newloc 

minx = 1e9
maxx = -1e9
miny = 1e9
maxy = -1e9
elves = 0
for i in loc.items():
    elves += 1
    key = i[0]
    if key[0] < minx:
        minx = key[0]
    if key[0] > maxx:
        maxx = key[0]
    if key[1] < miny:
        miny = key[1]
    if key[1] > maxy:
        maxy = key[1]

#print ((maxx-minx+1)*(maxy-miny+1)-elves)