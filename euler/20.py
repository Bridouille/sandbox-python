#!/usr/bin/python3.3

import sys

def fact(nb):
    if nb == 1:
        return nb
    return nb * fact(nb - 1)

def pb20():
    print(sum([int(k) for k in list(str(fact(100)))]))

if __name__ == "__main__":
    pb20()
