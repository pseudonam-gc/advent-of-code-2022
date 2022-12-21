import re
import itertools
import time

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


with open("inp19.txt") as f:
    c = [[int(j) for j in re.findall("-?\d+", i)] for i in f.readlines()]

optimal = [] # array of optimal values or something
for i in range(len(c)):
    optimal.append(0)

a = []
s = 0
for i in itertools.product(*(["1234"] * 14)):  # let a denote an ore robot and so on. this is the ordering of robots
    s += 1
    if s % int(1e7) == 0:
        print (s/1e7)
    if i[-1] == "4":
        if min(i.count("2"), i.count("3"), i.count("4")) > 0:
            if i.index("2") < i.index("3") < i.index("4"):
                if i.index("4") < 7:
                    a.append("".join(i))

# possible optimizations:
# it must end in a 4 since nothing else matters
# its first 3 must be after its first 2, its first 4 after its first 3

#a = ["221232234"]

for bindex, blueprint in enumerate(c): # for each blueprint
    print (bindex)
    best_4_index = 99
    memo = {}
    for i in a: # for each possible robot ordering
        #if i.index("4") > best_4_index+1:
            #continue
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
            #time.sleep(1)
            #print ("Round {}".format(round+1))
            #print ("Robots: {}".format(robots))
            #print ("Resources: {}".format(resources))
            if index != 0:
                memo[i[:index]] = (resources, robots, saved_round, robot_to_add)
        if resources[3] > optimal[bindex]:
            optimal[bindex] = resources[3]
            best_4_index = i.index("4")
            print (i)
print (optimal)
#print (memo)