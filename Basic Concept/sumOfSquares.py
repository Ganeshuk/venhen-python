def sumOfSquare():
    suM=0
    for i in n:
       suM+=i**2
    return suM

n=list(map(int,input().split(",")))
print(sumOfSquare())
