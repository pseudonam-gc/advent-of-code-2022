triples = set() # hash the triples lol
with open("inp18.txt") as f:
    c = [list([int(j) for j in i.strip().split(",")]) for i in f.readlines()]
    #print (c)
offsets = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 0, -1], [0, -1, 0], [-1, 0, 0]]
overlaps = 0
for i in c:
    triples.add(tuple(i))
"""for i in c:
    for j in offsets:
        if tuple([sum(x) for x in zip(i, j)]) in triples:
            overlaps += 1
        triples.add(tuple(i))
print (len(c)*6 - overlaps*2)"""

# so just simulate the water. LMAO. and count the neighbors of each waternode
water = [(0, 0, 0)]
index = 0
swater = set([(0, 0, 0)])

while index < len(water):
    for i in offsets:
        t = tuple([sum(x) for x in zip(water[index], i)])
        if t not in swater and t not in triples:
            if max(t) <= 25 and min(t) >= -2:
                swater.add(t)
                water.append(t)
    index += 1

for i in water:
    for j in offsets:
        if tuple([sum(x) for x in zip(i, j)]) in triples:
            overlaps += 1
print (overlaps)
# 2410 too low