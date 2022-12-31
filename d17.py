with open("inp17.txt") as f:
    s = f.read().strip()

"""####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""
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
"..#....",], 
[]]

grid = []
for i in range(7):
    grid.append(".......")
def height(grid):
    for i in range(len(grid)-1, 1, -1):
        if grid[i] != ".......":
            return i
    return 0

print (height(grid))