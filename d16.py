import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import time

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

cases = 0

def valve_search(current_valve, logbook=[], fixed_valves=[], energy=30, score=0):
    # note that the player literally can't go back. so there's that.
    maxval = score
    global cases
    cases += 1
    if cases % 10000 == 0:
        print (cases)
    #print ((current_valve, logbook, fixed_valves, energy, score))
    for i in valves[current_valve].distances:
        if energy-valves[current_valve].distances[i] > 0:
            v = valve_search(i, logbook+[current_valve], fixed_valves, energy-valves[current_valve].distances[i], score)
            if v > maxval:
                maxval = v
    if current_valve not in fixed_valves and energy > 0:
        v = valve_search(current_valve, logbook, fixed_valves+ [current_valve], energy-1, score+(energy-1)*valves[current_valve].flow)
        if v > maxval:
            maxval = v
    return maxval



with open("inp16.txt") as f:
    for line in f:
        l = line.strip().split()
        valves[l[1]] = Valve(l[1], int(l[4].split(";")[0][5:]), [i[0:2] for i in l[9:]])
        if valves[l[1]].flow > 0 or valves[l[1]].name == "AA":
            good_valves[l[1]] = valves[l[1]]
  
for i in good_valves:
    valves[i].setDistance()

pos=nx.spring_layout(G) 
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

print (valve_search("AA"))