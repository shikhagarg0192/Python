#!/bin/python
def displayPathtoPrincess(n,grid):
    print(grid[0][1])
    print(n)



m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
