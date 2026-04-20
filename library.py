import types
import json

app_name = "library"
version = "0.1"
is_active=True
book_count=0

def read_file(path:str) -> list:
    try:
        with open(path,"r",encoding="utf-8") as f:
            return json.load(f)
    except Exception as err:
        print(err)
        return []
library = read_file("./library.json")


def count(fn:types.FunctionType):
    def wrap(*args,**kwargs):
        wrap.counter+=1 # type: ignore
        return fn(*args,**kwargs)
    wrap.counter = 0 # type: ignore
    return wrap


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


@count
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
print(add_book.counter) # type: ignore


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

def book_iterator(genre_filter:str):
    for book in library:
        if book["genre"]== genre_filter:
            yield book


def write_to_json(library:list):
    try:
        with open("library.json","w",encoding="utf-8") as f:
            json.dump(library,f,ensure_ascii=False,indent=4)
    except Exception as err:
        print(err)

write_to_json(library)

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

class Ebook(Book):
    def __init__(self, title, author, year, genre="Unknown",filesize=0) -> None:
        super().__init__(title, author, year, genre)
        self.filesize = 0