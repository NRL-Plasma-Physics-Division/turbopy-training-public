acceptedinput=False
while not acceptedinput:
    try:
        maximum = int(input("What is the maximum value?"))
        if maximum >= 1:
            acceptedinput = True
        else:
            print("Positive Integer Required")
    except ValueError:
        print("Positive Integer Required")

NFir = 1
NSec = 1
print(0)
print(NFir)
print(NFir)
while NFir + NSec <= maximum:
    temporary = NFir + NSec
    print(temporary)
    NFir = NSec
    NSec = temporary
