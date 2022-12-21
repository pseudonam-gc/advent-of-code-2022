from sympy import *

x = symbols('x')

with open("inp21.txt") as f:
    c = [i.strip().split() for i in f.readlines()]
d={}
commands = []
for i in c:
    if len(i) == 2:
        if i[0][:4] == "humn":
            d[i[0][:4]] = x
        else: 
            d[i[0][:4]] = int(i[1])
    else:
        commands.append(i)
while len(commands) > 0:
    if "root" in d: 
        print (d["root"])
    for i in commands:
        if i[1] in d and i[3] in d:
            #print (i)
            #print (commands)
            if i[2] == "+":
                d[i[0][:4]] = d[i[1]]+d[i[3]]
            elif i[2] == "-":
                d[i[0][:4]] = d[i[1]]-d[i[3]]
            elif i[2] == "*":
                d[i[0][:4]] = d[i[1]]*d[i[3]]
            elif i[2] == "/":
                d[i[0][:4]] = d[i[1]]/d[i[3]]
            commands.remove(i)
            break
print (round(solve(d["root"], x)[0]))