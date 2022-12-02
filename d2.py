import math

with open("inp2.txt") as f:
    s = 0
    for line in f:
        l = line.strip()
        ab = l.split()
        a = ab[0]
        b = ab[1]
        if b == "X":
            s += 1
            if a == "A":
                s += 3
            if a == "B":
                s += 0
            if a == "C":
                s += 6
        if b == "Y":
            s += 2
            if a == "A":
                s += 6
            if a == "B":
                s += 3
            if a == "C":
                s += 0
        if b == "Z":
            s += 3
            if a == "A":
                s += 0
            if a == "B":
                s += 6
            if a == "C":
                s += 3
    print (s)
# part 2 code modification
"""if b == "X":
            s += 0
            if a == "A":
                s += 3
            if a == "B":
                s += 1
            if a == "C":
                s += 2
        if b == "Y":
            s += 3
            if a == "A":
                s += 1
            if a == "B":
                s += 2
            if a == "C":
                s += 3
        if b == "Z":
            s += 6
            if a == "A":
                s += 2
            if a == "B":
                s += 3
            if a == "C":
                s += 1"""
