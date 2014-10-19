#!/usr/bin/python3.3

def pb1():
    sum = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)


if __name__ == "__main__":
    pb1()
