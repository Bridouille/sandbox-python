#!/usr/bin/python3.3

def pb4():
    is_palindrome = lambda x : str(x) == str(x)[::-1]
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            produit = i * j
            if is_palindrome(str(produit)) == True and produit > max:
                max = produit
    print(max)

if __name__ == "__main__":
    pb4()
