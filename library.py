app_name = "library"
version = "0.1"
is_active=True
book_count=0

def create_book(title,author,year,genre="Unknown"):
    book = {
        "title":title,
        "author":author,
        "year":year,
        "genre":genre,
        "is_read":False
    }
    return book

def is_classic(book:dict):
    if book["year"] < 1950:
        return True
    return False

book1 = create_book("Kəlilə və Dimnə","Bilinmir",1949)
print(is_classic(book1))