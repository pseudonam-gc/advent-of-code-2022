with open("inp.txt") as f:
    c = f.read().split("\n")

print (c)
a = [0]
ind = 0 
for i in c:
    if i == "":
        ind += 1
        a.append(0)
    else:
        a[ind] += int(i)
b = []
b.append(max(a))
a.remove(max(a))
b.append(max(a))
a.remove(max(a))
b.append(max(a))
print (sum(b))