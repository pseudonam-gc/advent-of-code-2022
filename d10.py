with open("inp10.txt") as f:
    c = [i.split() for i in f.readlines()]
    cycle = 0
    x = 1
    cycles = [0]
    #print (c)
    for i in c:
        if i[0] == "noop":
            cycle += 1
            cycles.append(x)
        elif i[0] == "addx":
            cycle += 2
            cycles.append(x)
            x += int(i[1])
            cycles.append(x)
    for rows in range(6):
        s = ""
        for i in range(40):
            if abs(cycles[i+40*rows]-i) <= 1:
                s += "#"
            else:
                s += "."
        print (s)            
