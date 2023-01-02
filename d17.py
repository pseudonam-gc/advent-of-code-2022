with open("inp17.txt") as f:
    s = f.read().strip()

shapes = [
["..####."], 
[
"...#...",
"..###..", 
"...#..."], 
[
"....#..",
"....#..", 
"..###.."], 
[
"..#....",
"..#....",
"..#....",
"..#...."], 
[
"..##...",
"..##..."]]

grid = []
def addshape(grid, shape):
    for i in range(3):
        grid.append(".......")
    for i in range(len(shape)):
        grid.append(shape[len(shape)-i-1])
def height(grid):
    for i in range(len(grid)-1, 1, -1):
        if grid[i] != ".......":
            return i
    return 0
addshape(grid, shapes[0])
for i in range(len(grid)):
    print (grid[len(grid)-1-i])