class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return(f"title:{self.title},author:{self.author},pages:{self.pages}")
b=Book("warzone","bujji",12)
print(b.__str__())
