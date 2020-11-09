def fib():
    """
    Prints the Fibonacci numbers up to and including the user input
    """

    a = 0
    b = 1
    temp = 0
    limit = int(input("Enter the maximum Fibonacci number: "))
    while limit < 0:
        limit = int(input("Must be a positive number Please try again: "))
    while a <= limit:
        print(a)
        temp = a + b
        a = b
        b = temp


fib()
