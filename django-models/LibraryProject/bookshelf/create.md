from bookshelf.models import Book

book1 = Book.objects.create(title = '1984', author = 'George Orwell', publication_year = 1949)

book1.save()

print(book1)
<!-- 1984 by George Orwell published in 1949 -->
