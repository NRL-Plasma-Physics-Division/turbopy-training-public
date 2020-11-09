import sys

def fib(x):
    if(fib < 0):
        print("Negative numbers are not allowed.")
    if(fib == 0 or fib == 1):
        return 1;
    return fib(x-1) + fib(x-2);

n = sys.argv[1]
print(fib(n))
