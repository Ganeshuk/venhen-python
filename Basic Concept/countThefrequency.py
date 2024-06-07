n=input()
count={}
for i in range(len(n)):
    if n[i] in count:
        count[n[i]]=count[n[i]]+1
    else:
        count[n[i]]=1
print(count)