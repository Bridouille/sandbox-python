#!/usr/bin/python3.3

import sys, random

def genIsland(islands, x, y, density, maxX, maxY):
    if x >= 0 and x < maxX and y >= 0 and y < maxY and islands[y][x] == "." and density > 0:
        islands[y] = islands[y][:x] + "X" + islands[y][x + 1:]
        genIsland(islands, x - 1, y, random.randint(0, density - 1), maxX, maxY)
        genIsland(islands, x + 1, y, random.randint(0, density - 1), maxX, maxY)
        genIsland(islands, x, y - 1, random.randint(0, density - 1), maxX, maxY)
        genIsland(islands, x, y + 1, random.randint(0, density - 1), maxX, maxY)


def genIslands(x, y, density):
    islandsPos = [(random.randint(0, x - 1), random.randint(0, y - 1)) for k in range(density)]
    islands = ["." * x for k in range(y)]
    for pos in islandsPos:
        genIsland(islands, pos[0], pos[1], random.randint(1, density), x, y)
    for line in islands:
        print(line)

def printErr(errMsg):
    print(errMsg, file = sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        printErr("Usage : {} x y density".format(sys.argv[0]))
    else:
        try:
            genIslands(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        except ValueError as v:
            printErr(v)
