#!/usr/bin/python3.3

import sys, random

def genFile(x, y, density):
    if x <= 0 or y <= 0 or density <= 0:
        print("Each parameter need to be positive", file = sys.stderr)
        return
    print(y)
    for i in range(y):
        j = 0
        for j in range(x):
            print("o" if random.randint(0, y) * 2 < density else ".", end = "")
            j += 1
        print("")
        i += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : {} x y density".format(sys.argv[0]), file = sys.stderr)
    else:
        genFile(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
