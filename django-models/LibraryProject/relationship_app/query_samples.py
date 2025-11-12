from .models import Author, Book, Library, Librarian

#List all books in a library
def allBooksLibrary(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()

    for book in books:
        print(book.title)