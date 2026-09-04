#list operations

import json
import os
import sys

SCRIPT_DIR = os.path.expanduser("~/Pythonprac")
SAVE_FILE = os.path.join(SCRIPT_DIR, "mymenu_list.json")


if not os.path.exists(SCRIPT_DIR):
    try:
        os.makedirs(SCRIPT_DIR, exist_ok=True)
        print(f"[SYSTEM] Created missing directory: {SCRIPT_DIR}")
    except Exception as e:
        print(f"[ERROR] Could not create directory due to system permissions: {e}")

def load_list():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as file:
                data = json.load(file)
                print(f"\n[SYSTEM] Successfully loaded saved data: {data}")
                return data
        except json.JSONDecodeError:
            print("\n[Warning] Save file corrupted or empty. Starting fresh.")
            return []
    print("\n[SYSTEM] No previous save file detected. Starting with a blank list.")
    return []

def save_list():
    try:
        with open(SAVE_FILE, "w") as file:
            json.dump(lis, file)
            file.flush()               
            os.fsync(file.fileno())    
        print(f"[SYSTEM] Data permanently saved to file.")
    except Exception as e:
        print(f"[SYSTEM SAVE FAILURE]: {e}")

#assign to lis
lis = load_list()
    
def listadd():
    numelem = int(input("\nenter the number of items(integer only) youd like to put in the list: "))
    
    for i in range(0, numelem):
        a = int(input("enter the number: "))
        lis.append(a)
    save_list()
    print("\nthe list is now: ")
    print(lis)
    
def listmax():
    if not lis:
        print("\nempty list")
        return
    
    a = max(lis)
    print("\nthe maximum mumeral value within your list is: ", a)

def listmin():
    if not lis:
            print("\nempty list")
            return
        
    a = min(lis)
    print("\nthe minimum value within the list is: ", a)

def listindexprint():
    if not lis:
            print("\nempty list")
            return
        
    a = int(input("\nenter the index number you want to know: "))
    b = lis[a]
    print(f"\nyour index number is {a}, and the respective number is {b}.")

def lisprint():
    print("\n", lis)
    
def lisrem():
    if not lis:
            print("\nempty list")
            return
        
    p = int(input("\nenter the number of elments you'd like to remove: "))
    for i in range(0, p, 1):
        a = int(input("\nenter the  number youd like to remove from the list: "))
        b = input(f"\nconfirm removal of {a}? y/n. kindly use only y/n")
        if b == "n":
            print("\nterminated")
            return
        elif b == "y":
            lis.remove(a)
            print(f"\n{a} has been removed from the list")
    save_list()
    print("the list is now: ")
    print(lis)

def liseven():
    if not lis:
            print("\nempty list")
            return
        
    a = 0
    for i in lis:
        if i % 2 == 0:
            a += 1
            print("\n", a)
    print(f"\nthe total number of even items in list is {a}")
        
def lisodd():
    if not lis:
            print("\nempty list")
            return
        
    a = 0
    for i in lis:
        if i % 2 != 0:
            a += 1
            print("\n", a)
    print(f"\nthe total number of odd items in the list is {a}") 
    
def liscount():
    a = len(lis)
    print(f"\nthe number of items in the list is {a}")

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
      9. PRINT THE THE TOTAL ITEM COUNT
      10. EXIT THE PROCESS\n'''))

    try:
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
            liscount()
        elif finop == 10:
            print("data saved")
            break
        else:
            print("kindly select from 1 to 9 only")
    
    except ValueError:
        print("kindly enter a valid integer value between 1 and 9 as per the list")
        
    
            