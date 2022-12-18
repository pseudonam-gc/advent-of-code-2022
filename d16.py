import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import time
from operator import itemgetter

G = nx.Graph()

valves = {}
good_valves = {}

class Valve:
    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels
        self.distances = {}
    def setDistance(self): # find distance to all other valves 
        visited = []
        to_visit = [(self.name, 0)]
        while len(to_visit) > 0: # BFS: add everything to to_visit
            for i in valves[to_visit[0][0]].tunnels:
                if i in visited:
                    continue
                elif valves[i].flow > 0:
                    self.distances[valves[i].name] = to_visit[0][1]+1
                    continue
                else:
                    to_visit.append((i, to_visit[0][1]+1))
            visited.append(to_visit.pop(0)[0])
        print (self.name, len(self.distances))
        G.add_node(self.name)
        for i in self.distances:
            G.add_edge(self.name, i, weight=self.distances[i])

used_valves = []
valve_names = []

def valve_search(current_valve, valid_valves, logbook=[], fixed_valves=[], energy=26, score=0):
    # note that the player literally can't go back. so there's that.
    # optimal play is ('DG', ['AA', 'YW', 'OM', 'VX', 'WI', 'ZL', 'NG', 'IS'], ['YW', 'OM', 'VX', 'WI', 'ZL', 'NG', 'IS'], 1, 1751)
    # or, ('NG', ['AA', 'YW', 'OM', 'VX', 'WI', 'ZL'], ['YW', 'OM', 'VX', 'WI', 'ZL', 'NG'], 3, 1302)
    maxval = score
    #print ((current_valve, logbook, fixed_valves, energy, score))
    #if score == 1283 and len(valid_valves) == len(valves):
    #    print (logbook)
    #if score == 917 and len(valid_valves) != len(valves):
        #print (logbook)
    if 1100 <= score and len(valid_valves) == len(valves):
        used_valves.append((tuple(sorted(fixed_valves)), score))
    for i in valves[current_valve].distances:
        # make sure the received node is actually a node in a certain set, because it might not be for the elephant's movement
        if energy-valves[current_valve].distances[i] > 0:
            v = valve_search(i, valid_valves, logbook+[current_valve], fixed_valves, energy-valves[current_valve].distances[i], score)
            if v > maxval:
                maxval = v
    if current_valve not in fixed_valves and current_valve in valid_valves and energy > 0:
        v = valve_search(current_valve, valid_valves, logbook, fixed_valves+ [current_valve], energy-1, score+(energy-1)*valves[current_valve].flow)
        if v > maxval:
            maxval = v
    return maxval

with open("inp16.txt") as f:
    for line in f:
        l = line.strip().split()
        valves[l[1]] = Valve(l[1], int(l[4].split(";")[0][5:]), [i[0:2] for i in l[9:]])
        valve_names.append(l[1])
        if valves[l[1]].flow > 0 or valves[l[1]].name == "AA":
            #if valves[l[1]].name not in funny_nodes:
            good_valves[l[1]] = valves[l[1]]
  
for i in good_valves:
    valves[i].setDistance()

pos=nx.spring_layout(G) 
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#plt.show()

print (valve_search("AA", valve_names))
maxval = 0
counter = 0

end_search = 0

used_valves = list(set(used_valves))
used_valves = sorted(used_valves, key=itemgetter(1))[::-1]
#print (used_valves[:5])

print (len(used_valves))

for i in used_valves:
    counter += 1
    remaining_valves = [j for j in valve_names if j not in i[0]]
    b = valve_search("AA", remaining_valves)
    print (counter, i[1]+b)
    if i[1]+b > maxval:
        maxval = i[1]+b
        print ("optimal: " + str(maxval))
print (maxval)