d = {}

class Number():
    def __init__(self, index, value):
        self.index = index
        self.value = value

with open("inp20.txt") as f:
    c = [int(i.strip()) for i in f.readlines()]

d = {Number(index, i) for index, i in enumerate(c)}
l = [d[i] for i in range(len(c))]

for i in range(5000):
    l.remove(d[i])