#list operations

lis = []
    
def listadd():
    numelem = int(input("enter the number of numbes youd like to put in the list: "))
    
    for i in range(0, numelem):
        a = int(input("enter the number: "))
        lis.append(a)
    print("the list is now: ")
    print(lis)
    
def listmax():
    if not lis:
        print("empty list")
        return
    
    a = max(lis)
    print("the maximum mumeral value within your list is: ", a)

def listmin():
    if not lis:
            print("empty list")
            return
        
    a = min(lis)
    print("the minimum value within the list is: ", a)

def listindexprint():
    if not lis:
            print("empty list")
            return
        
    a = int(input("enter the index number you want to know: "))
    b = lis[a]
    print(f"your index number is {a}, and the respective number is {b}.")

def lisprint():
    print(lis)
    
def lisrem():
    if not lis:
            print("empty list")
            return
        
    p = int(input("enter the number of elments you'd like to remove: "))
    for i in range(0, p+1, 1):
        a = int(input("enter the  number youd like to remove from the list: "))
        b = input(f"confirm removal of {a}? y/n. kindly use only y/n")
        if b == "n":
            print("terminated")
            return
        elif b == "y":
            lis.remove(a)
            print(f"{a} has been removed from the list")

def liseven():
    if not lis:
            print("empty list")
            return
        
    a = 0
    for i in lis:
        if i % 2 == 0:
            a += 1
            print(a)
    print(f"the total number of even items in list is {a}")
        
def lisodd():
    if not lis:
            print("empty list")
            return
        
    a = 0
    for i in lis:
        if i % 2 != 0:
            a += 1
            print(a)
    print(f"the total number of odd items in the list is {a}") 

print("Hello!")

while True:
    finop = int(input('''\n----------CHOOSE THE OPERATION YOU WOULD LIKE TO PERFORM ON THE LIST----------
      1. ADD TO LIST
      2. REMOVE FROM LIST
      3. COUNT AND PRINT EVEN NUMBERS
      4. COUNT AND PRINT ODD NUMBERS
      5. PRINT THE LIST IN ITS CURRENT STATE
      6. PRINT THE LIST'S MAXIMUM VALUE
      7. PRINT THE LIST'S MINIMUM VALUE
      8. PRINT THE NUMBER CORRESPONDING TO A PARTICULAR INDEX
      9. EXIT THE PROCESS\n'''))

    if finop == 1:
        listadd()
    elif finop == 2:
        lisrem()
    elif finop == 3:
        liseven()
    elif finop == 4:
        lisodd()
    elif finop == 5:
        lisprint()
    elif finop == 6:
        listmax()
    elif finop == 7:
        listmin()
    elif finop == 8:
        listindexprint()
    elif finop == 9:
        break
    else:
        print("kindly enter a valid value")