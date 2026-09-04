#fizz for multple of 3, buzz for 5, fizzbuzz for both for numbers till 20

def fizzbuzz():
    i = 0
    while i <= 20:
        print(i)
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        i += 1
fizzbuzz()