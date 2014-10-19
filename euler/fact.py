#!/usr/bin/python3.3

import sys

def fact(nb):
    if nb == 1:
        return nb
    return nb * fact(nb - 1)

def main(av):
    if len(av) < 2:
        print("Usage : {} it".format(av[0]), file = sys.stderr)
    else:
        print(sum([int(k) for k in list(str(fact(int(av[1]))))]))

if __name__ == "__main__":
    main(sys.argv)
