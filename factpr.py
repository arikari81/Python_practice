#printing factoria
q1q = int(input("enter a number: "))

def fact(q1q):
    if q1q < 0:
        print("NEGATIVE NUMBERS DONT HAVE FACTORIALS.")
        return
        
    facto = 1
    for i in range(1, q1q+1):
        facto *= i
    
    print(f"the factorial of {q1q} is {facto}")
fact(q1q)