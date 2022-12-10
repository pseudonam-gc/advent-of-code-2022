sizes = []

class folder:
    def __init__(self, parent=-1):
        self.folders = {}
        self.files = {}
        self.parent = parent
        self.size = 0
    def updateSize(self):
        s = 0
        for i in self.files:
            s += self.files[i]
        for i in self.folders:
            s += self.folders[i].updateSize()
        sizes.append(s)
        return s
    def printFolder(self):
        print (self.folders, self.files)

with open("inp7.txt") as f:
    c = f.readlines()
    root = folder()
    line = 0
    current_folder = root
    while line < len(c):
        s = c[line].split() 
        if s[1] == "cd":
            if s[2] == "/":
                current_folder = root 
            elif s[2] == "..":
                current_folder = current_folder.parent
            else: 
                current_folder = current_folder.folders[s[2]]
            line += 1
        elif s[1] == "ls":
            # spam read the next however many lines
            line += 1
            s = c[line].split()
            while s[0] != "$": 
                if s[0] == "dir":
                    current_folder.folders[s[1]] = folder(current_folder)
                else:
                    current_folder.files[s[1]] = int(s[0])
                line += 1
                if line != len(c):
                    s = c[line].split()
                else:
                    break
    m=(root.updateSize())
    space=70000000-m
    for i in sorted(sizes):
        if space+i>= 30000000:
            print (i)
            break

    #print (sum([i if i <= 100000 else 0 for i in sizes])) <- day 1 solution