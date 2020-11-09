def fib(n):
    """
    Returns the nth term in the fib sequence
    
    Parameters
    ----------
    n : int
        The term in the fib sequence
        
        
    Returns
    -------
    int
        The nth term in the fib sequence
    """
    return 1 if n == 0 or n == 1 else fib(n - 1) + fib(n - 2)


num = int(input('what is n? '))
while num < 1:
    num = int(input('number must be > 1. what is n? '))

print(', '.join([str(fib(i)) for i in range(num)]))
