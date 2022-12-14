import math
from ast import literal_eval

def compare(a, b):
    #print ("comparing: " +str(a)+" "+ str(b))
    if type(a) == int and type(b) == int:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1 
    elif type(a) == list and type(b) == list:
        for i in range(min(len(a), len(b))):
            #print (i)
            c = compare(a[i], b[i])
            if c == -1:
                return -1
            elif c == 1:
                return 1
            # otherwise, they're equal and keep going
        if len(a) < len(b):
            return -1
        elif len(b) < len(a):
            return 1
        else:
            return 0
    else:
        if type(a) == int:
            return compare([a], b)
        if type(b) == int:
            return compare(a, [b])

with open("inp13.txt") as f: 
    c = [literal_eval(i.strip()) for i in f.readlines() if i != "\n"]
    for i in range(len(c)):
        for j in range(len(c)):
            if i != j:
                if compare(c[i], c[j]) == -1:
                    t = c[i]
                    c[i] = c[j]
                    c[j] = t
    twoindex = -1
    sixindex = -1
    for i in range(len(c)):
        if c[i] == [[2]]:
            twoindex = i+1
        if c[i] == [[6]]:
            sixindex = i+1
    print (twoindex*sixindex)
    """s = 0
    for i in range(math.ceil(len(c)/3)):
        a = literal_eval(c[i*3])
        b = literal_eval(c[i*3+1])
        if compare(a, b) == -1:
            s += (i+1)
            print (str(i+1)+" is ordered")
        else:
            print (str(i+1)+" is NOT ordered")
        #print (a, b)
    print (s)"""