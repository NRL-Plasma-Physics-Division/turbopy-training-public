"""
This program takes a user input and prints all fibonacci numbers less than or equal to that input.
"""

fibMax = int(input("How high do you want the sequence to go? "))

def fibonacci(max):
    """
    Returns all fibonacci numbers less than or equal to a given input
    
    Parameters
    ----------
    max : int, float
        Maximum value, all returned values will be less than or equal to `max`

    Returns
    -------
    list
        All fibonacci numbers less than or equal to `max` in a list in ascending order
    """
    if max < 0:
        return "Sorry, enter a positive integer."
    elif max == 0:
        return [0]
    a = 0
    b = 1
    fib = []
    while b <= max:
        a, b = b, a+b
        fib.append(a)
    return fib

print(fibonacci(fibMax))
