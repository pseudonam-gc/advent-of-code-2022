import re
import itertools
import time

with open("inp19.txt") as f:
    c = [[int(j) for j in re.findall("-?\d+", i)] for i in f.readlines()]

optimal = [] # array of optimal values or something
for i in range(len(c)):
    optimal.append(0)

memo = []

def construct(blueprint, resources, type):
    res = resources
    if type == 1:
        if res[0] >= blueprint[1]:
            res[0] -= blueprint[1]
            return res 
        else:
            return -1
    if type == 2:
        if res[0] >= blueprint[2]:
            res[0] -= blueprint[2]
            return res 
        else:
            return -1
    if type == 3:
        if res[0] >= blueprint[3] and res[1] >= blueprint[4]:
            res[0] -= blueprint[3]
            res[1] -= blueprint[4]
            return res 
        else:
            return -1
    if type == 4:
        if res[0] >= blueprint[5] and res[2] >= blueprint[6]:
            res[0] -= blueprint[5]
            res[2] -= blueprint[6]
            return res 
        else:
            return -1
    return -1

a0 = []
a1 = []
a2 = []
a3 = []
s = 0
for i in itertools.product(*(["234"] * 9)):  # 15 would be enough. of course screw this lmao
    s += 1
    if s % int(1e6) == 0:
        print ("progress: " + str(s/1e6))
    if i[-1] == "4":
        if min(i.count("2"), i.count("3"), i.count("4")) > 0:
            if i.index("2") < i.index("3") < i.index("4"):
                if i.index("4") < 7:
                    a0.append("".join(i))
for i in range(len(a0)):
    for j in range(len(a0[i])+1):
        a1.append(a0[i][:j] + "1" + a0[i][j:])
for i in range(len(a1)):
    for j in range(len(a1[i])+1):
        a2.append(a1[i][:j] + "1" + a1[i][j:])
a2 = list(set(a2))
for i in range(len(a2)):
    for j in range(len(a2[i])+1):
        a3.append(a2[i][:j] + "1" + a2[i][j:])
a3 = list(set(a3))

for bindex, blueprint in enumerate(c): # for each blueprint
    print ("Test case: "+str(bindex))
    best_4_index = 99
    memo = {}
    m = max(blueprint[1], blueprint[2], blueprint[3], blueprint[5])
    print ("Max: "+str(m))
    if m == 2:
        a = a1
    elif m == 3:
        a = a2
    else: 
        a = a3
    for i in a: # for each possible robot ordering
        resources = [0, 0, 0, 0]
        robots = [1, 0, 0, 0]
        robot_to_add = -1
        saved_round = 0
        index = 0
        if i[:index] in memo:
            resources, robots, saved_round, robot_to_add = memo[i[:index]]
            continue
        for round in range(saved_round, 24):
            for j in range(4): 
                resources[j] += robots[j]
            if robot_to_add != -1:
                robots[robot_to_add-1] += 1
                robot_to_add = -1
            if index < len(i):
                res = construct(blueprint, resources, int(i[index]))
                if res != -1:
                    resources = res
                    robot_to_add = int(i[index])
                    index += 1
            if index != 0:
                memo[i[:index]] = (resources, robots, saved_round, robot_to_add)
        if resources[3] > optimal[bindex]:
            optimal[bindex] = resources[3]
            best_4_index = i.index("4")
            print (i)
            print (optimal)
print ("optimal geodes: " + str(optimal))