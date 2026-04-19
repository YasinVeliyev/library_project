app_name = "library"
version = "0.1"
is_active=True
book_count=0
library = []

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


def book_era(book:dict)  -> bool|str:
    if book["year"] > 2000:
        return "New"
    return True


def add_book(book:dict) -> None:
    # global library
    library.append(book)
    print(f"{book["title"]}  {len(library)}")


def remove_book(title:str) -> None :
    for book in library:
        if book["title"]==title:
            library.remove(book)
            break
    else:
        print(f"Book with {title} not found")


add_book(create_book("Əli və Nino", "Qurban Səid", 1937, "Roman"))
add_book(create_book("1984", "George Orwell", 1949, "Distopiya"))
add_book(create_book("Sapiens", "Yuval Noah Harari", 2011, "Tarix"))

book_id = ("ISBN-001", "Əli və Nino")
print(f"ID tuple: {book_id}")

def get_all_genres() -> set:
    genres = set()
    for book in library:
        genres.add(book["genre"])
    return genres


my_genres = {"Roman", "Tarix", "Fantastika"}
friend_genres = {"Roman", "Detektiv", "Fantastika"}
print("Ortaq:", my_genres & friend_genres)
print("Birləşmə:", my_genres | friend_genres)
print("Fərq:", my_genres - friend_genres)

classic_books = [book["title"] for book in library if is_classic(book)]
print(f"Theese are classic books : {classic_books}")

authors = [book["author"] for book in library ]

print(f"Theese are authors : {authors}")


class Book:
    def __init__(self,title,author,year,genre="Unknown") -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True
    

class Library:
    def __init__(self) -> None:
        self.books = []
    

    def add_book(self,book:Book):
        self.books.append(book)
    
    def show_all_books(self):
        pass