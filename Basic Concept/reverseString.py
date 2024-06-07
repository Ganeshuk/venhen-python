# reverse string,It is done in two ways 
# 1

word=input()
print(word[::-1])

#2 
def reverse(word):
    reverse_word=""
    for  i in range(len(word)):
        reverse_word=word[i]+reverse_word
    return reverse_word 
print(reverse(word))