import numpy as np
with open("inp8.txt") as f:
    c = [i.strip() for i in f.readlines()]
    c = np.array([[int(j) for j in i] for i in c])
    print (c)
# part 1
"""
s=0
for i in range(len(c)):
    for j in range(len(c[i])):
        if i == 0 or i == len(c)-1 or j == 0 or j == len(c[i])-1:
            s += 1
        else:
            if c[i,j] > np.max(c[:i,j]) or c[i,j] > np.max(c[(i+1):,j]) or c[i,j] > np.max(c[i,(j+1):]) or c[i,j] > np.max(c[i,:j]):
                s += 1
print (s)
        """
# part 2
mx = 0
for i in range(1, len(c)-1):
    for j in range(1, len(c[i])-1):
        l, r, u, d = 0, 0, 0, 0
        a=i
        while a == i or (a > 0 and c[a, j] < c[i, j]):
            a -= 1
            u += 1
        a=i
        while a == i or (a < len(c)-1 and c[a, j] < c[i, j]):
            a += 1
            d += 1
        b=j
        while b == j or (b > 0 and c[i, b] < c[i, j]):
            b -= 1
            l += 1
        b=j
        while b == j or (b < len(c[i])-1 and c[i, b] < c[i, j]):
            b += 1
            r += 1
        
        if l*r*u*d>mx: 
            mx=l*r*u*d
print (mx)