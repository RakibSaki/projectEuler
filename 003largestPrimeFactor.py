import sys
def askandanswer():
    primefactors = set()
    largestprimefactor=1
    primenumbers = set()
    primenumbers.add(2)
    x=None
    while x==None:
        inp = input("Number: ")
        try:
            x=int(inp)
        except ValueError:
            if inp == "Thanks":
                print("You're welcome ;D")
                sys.exit()
            else:
                print("wrong input, please enter a NUMBER")
    
    originalx = x+0
    for i in range(2, int(x / 2)+1):
        if (x % i == 0):
            largestprimefactor=i
            while x%i == 0 and x!=i:
                x = x / i
        if i >= x:
            break
    if largestprimefactor==1:
        print(f"{originalx} is a prime number")
    else:
        print(f"The largest prime factor of {originalx} is {largestprimefactor}")
    askandanswer()
askandanswer()