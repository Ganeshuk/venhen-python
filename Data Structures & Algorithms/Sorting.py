n=list(map(int,input().split(",")))
# sorting ascending order
for i in range(len(n)):
    for j in range(i,len(n)):
        if n[i]>n[j]:
            n[i],n[j]=n[j],n[i]
print(n)

# descending order
for i in range(len(n)):
    for j in range(i,len(n)):
        if n[i]<n[j]:
            n[i],n[j]=n[j],n[i]
print(n)