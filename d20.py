class Node:
    def __init__(self, value, activation):
        self.value = value
        self.activation = activation

with open("inp20.txt") as f:
    c = [int(i.strip()) for i in f.readlines()]

circ = []
for i in range(len(c)):
    circ.append(Node(c[i]*811589153, i))

for round in range(10):
    print (round)
    for i in range(len(c)):
        for j in range(len(c)):
            if circ[j].activation == i:
                temp = circ[j]
                circ.pop(j)
                circ.insert((temp.value+j) % (len(c)-1), temp)
                break

for i in range(len(c)):
    if circ[i].value == 0:
        print (circ[(i+1000)%len(c)].value+circ[(i+2000)%len(c)].value+circ[(i+3000)%len(c)].value)
