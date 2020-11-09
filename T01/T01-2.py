n = int(input("Upper bound?")) #Asks the user for the highest number they want to display
if n <= 0:
    raise Exception("Upper bound must be positive") # Raises an exception if n is negative
a = 0
b = 1
print(a)
print(b) # These lines take care of displaying the first 2 fibonacci numbers
while b + a <= n: # Continues to print fibonacci numbers until the next loop will produce a number > n
    temp = a # Creates a temporary variable that points to the same value as a
    a = b # a now points to the same value as b
    b = a + temp # This line is equivalent to b = b + a or b += a, produces the next fibonacci number
    print(b) # Prints b 
