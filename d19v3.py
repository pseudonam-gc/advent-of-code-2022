import re
import itertools
import time
from copy import deepcopy 

with open("inp19.txt") as f:
    c = [[int(j) for j in re.findall("-?\d+", i)] for i in f.readlines()]

def value(inp):  
    mats = inp[0]
    robots = inp[1]
    return (mats[3]+robots[3]*(31-time))*10000+(mats[2]+robots[2]*(31-time))*100+(mats[1]+robots[1]*(31-time))*1+(mats[0]+robots[0]*(31-time))

quality = 1

for index, blueprint in enumerate(c[:3]):
    print ("BP: {a}".format(a=index))
    poss = [((0, 0, 0, 0), (1, 0, 0, 0))] # list of possibilities 
    for time in range(32):
        #print ("T: {a}".format(a=time))
        queue = []
        for mats, robots in poss:
            cond1 = (mats[0] >= blueprint[1])
            cond2 = (mats[0] >= blueprint[2])
            cond3 = (mats[0] >= blueprint[3] and mats[1] >= blueprint[4])
            cond4 = (mats[0] >= blueprint[5] and mats[2] >= blueprint[6])
            if cond1:
                m, r = list(mats), list(robots)
                for i in range(4):
                    m[i] += r[i]
                m[0] -= blueprint[1]
                r[0] += 1
                queue.append((tuple(m), tuple(r)))
            if cond2:
                m, r = list(mats), list(robots)
                for i in range(4):
                    m[i] += r[i]
                m[0] -= blueprint[2]
                r[1] += 1
                queue.append((tuple(m), tuple(r)))
            if cond3:
                m, r = list(mats), list(robots)
                for i in range(4):
                    m[i] += r[i]
                m[0] -= blueprint[3]
                m[1] -= blueprint[4]
                r[2] += 1
                queue.append((tuple(m), tuple(r)))
            if cond4:
                m, r = list(mats), list(robots)
                for i in range(4):
                    m[i] += r[i]
                m[0] -= blueprint[5]
                m[2] -= blueprint[6]
                r[3] += 1
                queue.append((tuple(m), tuple(r)))
            # check what things can ever be made
            rats = list(mats)
            for i in range(4):
                rats[i] += 100*robots[i]
            grond1 = (rats[0] >= blueprint[1])
            grond2 = (rats[0] >= blueprint[2])
            grond3 = (rats[0] >= blueprint[3] and rats[1] >= blueprint[4])
            grond4 = (rats[0] >= blueprint[5] and rats[2] >= blueprint[6])
            # ensure that 'do nothing' isn't an option if everything can be made that can be made
            if [cond1, cond2, cond3, cond4] != [grond1, grond2, grond3, grond4]:
                m, r = list(mats), list(robots)
                for i in range(4):
                    m[i] += r[i]
                queue.append((tuple(m), tuple(r)))
        
        valid = []
        queue = list(set(queue))
        for mats, robots in queue:
            if robots[0] <= max(blueprint[1], blueprint[2], blueprint[3], blueprint[5]) and robots[1] <= blueprint[4] and robots[2] <= blueprint[6]: 
                valid.append((mats, robots))
        valid.sort(key = value)
        valid = valid[::-1]
        poss = valid[:min(len(valid), 100000)]

    quality *= max([i[0][3] for i in poss])
    print (max([i[0][3] for i in poss]))
print (quality)