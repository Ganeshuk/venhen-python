n=[1,2,2,1,2,32,1,1,32]

def find_duplicates():
    orginal=[]
    duplicate=[]
    for i in n:
        if i in orginal:
            if i not in duplicate:
                duplicate.append(i)
        else:
            orginal.append(i)
    return duplicate
            
print(find_duplicates())   