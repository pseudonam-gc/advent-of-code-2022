import re
s = 0
with open("inp4.txt") as f:
    l = [i.strip() for i in f.readlines()]
    for i in l:
        a = [int(x) for x in re.split(r',|-', i)]
        if a[0] <= a[2] <= a[1] or a[0] <= a[3] <= a[1] or a[2] <= a[0] <= a[3] or a[2] <= a[1] <= a[3]:
        #if a[0] <= a[2] <= a[3] <= a[1] or a[2] <= a[0] <= a[1] <= a[3]: day 1 code
            s += 1

    print (s)