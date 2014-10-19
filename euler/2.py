#!/usr/bin/python3.3

def pb2():
    n, n2, sum = 1, 1, 0
    while n <= 4000000:
        n, n2 = n2, n + n2
        if n % 2 == 0:
            sum += n
    print(sum)

if __name__ == "__main__":
    pb2()
