#counting the given number of voiwels in a particular file

def vowcount():
    vow = "aeiouAEIOU"
    count = 0
    f = open("vowcountsample.txt", "r")
    r = f.read()
    x = r.split()
    for i in x:
        for j in i:
            if j in vow:
                count += 1
    print(f"the total number of vowels in this file is {count}")
vowcount()