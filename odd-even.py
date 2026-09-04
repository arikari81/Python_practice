#odd-even tester
def checkoddev():
    num1 = int(input("enter a number: "))
    
    if num1 % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")
    
    if num1 % 5 == 0:
        print("huzzah, its a mutliple of 5")
        
checkoddev()