d = {}

class Number():
    def __init__(self, index, value):
        self.index = index
        self.value = value

with open("inp20.txt") as f:
    c = [int(i.strip()) for i in f.readlines()]

#d = {index:i for index, i in enumerate(c)} 
d = {index:Number(index, i) for index, i in enumerate(c)} # dictionary used just to find ordering i suppose
l = [d[i] for i in range(len(c))]

for i in range(5):
    # we want to shift d[i] 
    l.insert((d[i].index)%5, l.pop(d[i]))