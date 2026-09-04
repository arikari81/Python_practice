def checkpal():
    num1 = int(input("enter the number to be checked: "))    
    if num1 < 0:
        print("not a palindrom, since it is negative")
    
    original = num1
    reversed_num = 0
    
    while num1 > 0:
        reversed_num = (reversed_num * 10) + (num1 % 10)
        num1 //= 10
        
    if original == reversed_num:
        print("the number is a palindrome")
checkpal()