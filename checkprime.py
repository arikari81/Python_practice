#checking prime
plum = int(input("enter the number to be checked: "))
def checkprime(plum):
    for i in range(2, plum, 1):
        if plum % i == 0:
            return "not prime"
        else:
            return "prime number"
print(checkprime(plum))