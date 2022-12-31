import numpy as np

with open("inp25.txt") as f:
    c = [i.strip() for i in f.readlines()]
s = 0
for i in c:
    n = 0
    for index, j in enumerate(i):
        if j in ["0", "1", "2"]: 
            n += int(j)*5**(len(i)-index-1)
        elif j == "-":
            n += -1*5**(len(i)-index-1)
        else:
            n += -2*5**(len(i)-index-1)
    s += n
print (s)
string = ""
while s > 0:
    value = int(s % 5)
    character = value
    if value == 4:
        value = -1
        character = "-"
    if value == 3:
        value = -2
        character = "="
    s -= value 
    s /= 5
    string = str(character) + string 

print (string)
