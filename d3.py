with open("inp3.txt") as f:
    s = 0
    l = [i.strip() for i in f.readlines()]
    """part 1 sol
    l = line.strip()
        a = {i for i in l[:int(len(l)/2)]}
        b = {i for i in l[int(len(l)/2):]}
        m = list(a.intersection(b))
        if m != []:
            if ord(m[0])>=ord('a'):
                s += ord(m[0])-ord('a')+1
            else:
                s += ord(m[0])-ord('A')+27
            print (s)
    print (s)"""
    print(l)
    for i in range(int(len(l)/3)):
        a = set([i for i in l[i*3+0]])
        b = set([i for i in l[i*3+1]])
        c = set([i for i in l[i*3+2]])
        m = list(a.intersection(b.intersection(c)))
        if ord(m[0])>=ord('a'):
            s += ord(m[0])-ord('a')+1
        else:
            s += ord(m[0])-ord('A')+27
    print (s)