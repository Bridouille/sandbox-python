#!/usr/bin/python3.3

import sys, os

def markIsland(islands, x, y, nbIslands, maxX, maxY):
    if x >= 0 and x < maxX and y >= 0 and y < maxY and islands[y][x] == 'X':
        islands[y][x] = str(nbIslands)
        markIsland(islands, x - 1, y, nbIslands, maxX, maxY)
        markIsland(islands, x + 1, y, nbIslands, maxX, maxY)
        markIsland(islands, x, y - 1, nbIslands, maxX, maxY)
        markIsland(islands, x, y + 1, nbIslands, maxX, maxY)

def checkFile(islands):
    if len(islands) < 2:
        printErr("{}: file is too short".format(sys.argv[0]))
        sys.exit(1)
    sizeLine = len(islands[0])
    for line in islands:
        if len(line) != sizeLine:
            printErr("{}: file is not well formated".format(sys.argv[0]))
            sys.exit(1)
    return sizeLine, len(islands)

def countIslands(islands):
    nbIslands, y = 0, 0
    maxX, maxY = checkFile(islands)
    for line in islands:
        x = 0
        for letter in line:
            if letter == 'X':
                nbIslands += 1
                markIsland(islands, x, y, nbIslands, maxX, maxY)
            x += 1
        y += 1

    for line in islands:
        print("".join(line))

def printErr(errMsg):
    print(errMsg, file = sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        printErr("Usage : {} file_with_islands_to_count".format(sys.argv[0]))
    else:
        try:
            islands = [list(line.strip()) for line in open(sys.argv[1], "r").readlines()]
            countIslands(islands)
        except IOError as e:
            printErr("{}: {}: {}".format(sys.argv[0], sys.argv[1], os.strerror(e.errno)))
