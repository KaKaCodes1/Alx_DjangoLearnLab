from .models import Author, Book, Library, Librarian

#List all books in a library
def allBooksLibrary(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()

    for book in books:
        print(book)

#Query all books by a specific author
def allBooksByAuthor(author_name):
    author_name = Author.objects.get(name = author_name)
    books = Book.objects.filter(author = author_name)

    for book in books:
        print(book)

#Retrieve the librarian for a library
def getlibrarian(library_name):
    library = Library.objects.get(name=library_name)
    