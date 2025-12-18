# Import necessary tools for testing
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):

    # Set up the test environment before each test
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Create an author for the foreign key requirement
        self.author = Author.objects.create(name="J.K. Rowling")
        # Create a book to test update/delete/detail
        self.book = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)
        
        # Match these names EXACTLY to your urlpatterns in urls.py
        self.list_url = reverse('books-list') 
        self.create_url = reverse('books-create')
        self.detail_url = reverse('books-detail', kwargs={'pk': self.book.pk})
        self.update_url = reverse('books-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('books-delete', kwargs={'pk': self.book.pk})

    # Test retrieving the list of books
    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test creating a book while logged in
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        data = {"title": "The Hobbit", "publication_year": 1937, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test permission: Unauthenticated users cannot create
    def test_create_book_unauthenticated(self):
        data = {"title": "Forbidden", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test updating a book (PUT)
    def test_update_book(self):
        self.client.login(username='testuser', password='password123')
        data = {"title": "Harry Potter Updated", "publication_year": 1997, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test deleting a book (DELETE)
    def test_delete_book(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Test Filtering
    def test_filter_by_year(self):
        response = self.client.get(self.list_url, {'publication_year': 1997})
        self.assertEqual(len(response.data), 1)

    # Test Searching
    def test_search_by_title(self):
        response = self.client.get(self.list_url, {'search': 'Harry'})
        self.assertEqual(len(response.data), 1)

    # Test Ordering
    def test_ordering_by_year(self):
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)