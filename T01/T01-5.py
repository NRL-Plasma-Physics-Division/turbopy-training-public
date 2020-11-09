"""Use a generator function to compute Fibonacci numbers.

This code shows how to use a python generator to compute the 
Fibonacci numbers.

I'm also using this to test writing docstrings in numpydoc format.
"""

def fibonacci():
    """Generator of Fibonacci numbers.
    
    A python generator function to compute Fibonacci numbers.
    
    Yields
    ------
    int
        The next Fibonacci number in the sequence.
    
    Example
    -------
    >>> fib = fibonacci()
    >>> for m in range(10):
    >>>     print(next(fib))
    
    Notes
    -----
    The Fibonacci numbers are defined through the recursion relation:
    
    .. math:: F_n = F_{n-1} + F_{n-2}
    
    where :math:`F_0 = 0, F_1 = 1` and :math:`n \gt 1`.
    
    For more information about the Fibonacci numbers, see
    `the wikipedia page <https://en.wikipedia.org/wiki/Fibonacci_number>`_.
        
    This function is based on the example code here:
    https://book.pythontips.com/en/latest/generators.html
    and here:
    https://www.csestack.org/python-fibonacci-generator/
    """
    a = 0
    b = 1
    while(True):
        yield b
        a, b = b, a + b


if __name__ == "__main__":
    print(help(fibonacci))
    
    ordinal = {1: 'st', 2: 'nd', 3: 'rd'}
    
    # This example shows how to compute 10 Fibonacci numbers
    fib = fibonacci()
    for m in range(10):
        print(f"The {m+1}{ordinal.get(m+1,'th')} Fibonacci number is {next(fib)}")
        
    # This example shows how to compute all the Fibonacci numbers less than 10
    fib = fibonacci()
    m = next(fib)
    while m < 10:
        print(f"The next Fibonacci number is {m}")
        m = next(fib)
        
    