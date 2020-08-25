x = int(input("Number: "))
x = x - 1
multiplesof3=int(x/3)
multiplesof5=int(x/5)
multiplesof15=int(x/15)
def sumofthatmanymultiples(n, a):
    return (n+1)*(a*n)/2
answer=sumofthatmanymultiples(multiplesof3, 3) + sumofthatmanymultiples(multiplesof5, 5) - sumofthatmanymultiples(multiplesof15, 15)
print(f"Sum of all multiples of 3 or 5 under {x+1} is {answer}")