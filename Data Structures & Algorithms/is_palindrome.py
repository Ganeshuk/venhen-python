n=input()
def is_palindrome():
    reverse_word=""
    for  i in range(len(n)):
        reverse_word=n[i]+reverse_word
    return reverse_word==n 
print(is_palindrome())