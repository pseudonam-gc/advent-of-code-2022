def move(l1, l2, n):
    x = l1[:n] # just reverse this for part 1
    l1[:] = l1[n:]
    l2[:] = x + l2 

with open("inp5.txt") as f:
    l = [i.strip().split() for i in f.readlines()]
    stacks=[]
    stacks.append([i for i in "LCGMQ"]) 
    stacks.append([i for i in "GHFTCLDR"])
    stacks.append([i for i in "RWTMNFJV"])
    stacks.append([i for i in "PQVDFJ"])
    stacks.append([i for i in "TBLSMFN"])
    stacks.append([i for i in "PDCHVNR"])
    stacks.append([i for i in "TCH"])
    stacks.append([i for i in "PHNZVJSG"])
    stacks.append([i for i in "GHFZ"])
    for i in l:
        move(stacks[int(i[3])-1], stacks[int(i[5])-1], int(i[1]))
    print (stacks)
