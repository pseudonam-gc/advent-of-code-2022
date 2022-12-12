import math
insp = [0, 0, 0, 0, 0, 0, 0, 0]
with open("inp11.txt") as f:
    invs = [[85,77,77],[80,99],[74, 60, 74, 63, 86, 92, 80],[71, 58, 93, 65, 80, 68, 54, 71],[97, 56, 79, 65, 58],[77],[99, 90, 84, 50],[50, 66, 61, 92, 64, 78]]
    for i in range(10000): # rounds
        print (i)
        for j in range(len(invs)): # monkeys
            while len(invs[j]) != 0:
                insp[j] += 1
                invs[j][0] = invs[j][0] % (2*3*5*7*11*13*17*19)
                if j == 0:
                    invs[j][0] *= 7
                    if invs[j][0] % 19 == 0:
                        invs[6].append(invs[j][0])
                    else:
                        invs[7].append(invs[j][0])
                    invs[j].pop(0)
                elif j == 1:
                    invs[j][0] *= 11
                    if invs[j][0] % 3 == 0:
                        invs[3].append(invs[j][0])
                    else:
                        invs[5].append(invs[j][0])
                    invs[j].pop(0)
                elif j == 2:
                    invs[j][0] += 8
                    if invs[j][0] % 13 == 0:
                        invs[0].append(invs[j][0])
                    else:
                        invs[6].append(invs[j][0])
                    invs[j].pop(0)
                elif j == 3:
                    invs[j][0] += 7
                    if invs[j][0] % 7 == 0:
                        invs[2].append(invs[j][0])
                    else:
                        invs[4].append(invs[j][0])
                    invs[j].pop(0)
                elif j == 4:
                    invs[j][0] += 5
                    if invs[j][0] % 5 == 0:
                        invs[2].append(invs[j][0])
                    else:
                        invs[0].append(invs[j][0])
                    invs[j].pop(0)
                elif j == 5:
                    invs[j][0] += 4
                    if invs[j][0] % 11 == 0:
                        invs[4].append(invs[j][0])
                    else:
                        invs[3].append(invs[j][0])
                    invs[j].pop(0)
                elif j == 6:
                    invs[j][0] *= invs[j][0]
                    if invs[j][0] % 17 == 0:
                        invs[7].append(invs[j][0])
                    else:
                        invs[1].append(invs[j][0])
                    invs[j].pop(0)
                elif j == 7:
                    invs[j][0] += 3
                    if invs[j][0] % 2 == 0:
                        invs[5].append(invs[j][0])
                    else:
                        invs[1].append(invs[j][0])
                    invs[j].pop(0)
    insp.sort()
    print (insp[7]*insp[6])