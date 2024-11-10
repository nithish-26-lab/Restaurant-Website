def fib(n):
    if n <= 0:
        return "Invalid"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def pfib(n):
    if n <= 0:
        print("invalid")
    else:
        for i in range(1, n+1):
            print(fib(i), end = " ")
n = int(input())
pfib(n)