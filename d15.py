import re

with open("inp15.txt") as f:
    c = [[int(j) for j in re.findall("-?\d+", i)] for i in f.readlines()]
    sensors = [[i[0], i[1], abs(i[2]-i[0])+abs(i[3]-i[1])] for i in c] # in the form [a, b, distance]
    print (sensors)
    for row in range(0, 4000000):
        if row % 10000 == 0:
            print (row)
        pairwise = [[i[0]-i[2]+abs(row-i[1]), i[0]+i[2]-abs(row-i[1])] for i in sensors if abs(row-i[1]) <= i[2]]
        pairwise.sort()
        disjointpairs = [pairwise[0]]
        for i in range(1, len(pairwise)):
            if disjointpairs[-1][1] < pairwise[i][0]-1:
                disjointpairs.append(pairwise[i])
            else:
                disjointpairs[-1][1] = max(disjointpairs[-1][1], pairwise[i][1])
        for i in disjointpairs:
            if 0 < i[0] < 4000000:
                print ("ANSWER: " + str(i[0]-1)+ " "+str(row))
        """distances = (sum([abs(i[0]-i[1])+1 for i in disjointpairs]))
        beacons_on_row = {(i[2], i[3]) for i in c if i[3] == row}
        beacons_in_distances = 0
        for i in beacons_on_row:
            for j in disjointpairs:
                if j[0] <= i[1] <= j[1]:
                    beacons_in_distances += 1
        print (distances-beacons_in_distances)"""