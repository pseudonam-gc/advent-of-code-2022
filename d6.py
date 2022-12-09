with open("inp6.txt") as f:
    c = f.readlines()[0]
    for i in range(0, len(c)-14):
        if len(set(c[i:(i+14)])) == 14:
            print (i+14)
            break 