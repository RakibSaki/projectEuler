n = int(input())
previousterm=1
currentterm=1
sumtillnow=0
while currentterm <= n:
    print(currentterm)
    if currentterm % 2 == 0:
        sumtillnow = sumtillnow + currentterm
    previousterm, currentterm = currentterm, previousterm + currentterm

print(sumtillnow)