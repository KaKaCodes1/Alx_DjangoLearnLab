from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def has_permissions(self):
    #     if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
    #         permission_classes = [IsAuthenticated] #Any logged-in user (token required) can view books
    #     else:
    #         permission_classes = [IsAdminUser] #only Admin users can use POST, PUT, PATCH, DELETE

    #     return [permission() for permission in permission_classes]

    """
    A ViewSet for viewing and editing book instances.
    - GET (list/retrieve) is allowed for any user (unauthenticated).
    - POST, PUT, PATCH, DELETE require the user to be authenticated via token.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
