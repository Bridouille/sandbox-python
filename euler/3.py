#!/usr/bin/python3.3

import sys

def pb3(nb):
    for i in range(1, int(nb**0.5) + 1):
        if nb % i == 0:
            nb /= i
            last = i
    print(last)

if __name__ == "__main__":
    pb3(600851475143)


