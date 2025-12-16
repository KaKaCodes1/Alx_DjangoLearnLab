from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList,BookViewSet

#The router will handle creating the appropriate URL patterns
# for all CRUD operations on the Book model.
router = DefaultRouter()
router.register(r'books_all',BookViewSet, basename='book_all' )

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('',include(router.urls)),

    # Users will POST their username/password to this URL to get their token.
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    
]