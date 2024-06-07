def is_prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
             c+=1 
    return c==2

n=int(input())
print(is_prime(n))