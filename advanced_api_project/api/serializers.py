from rest_framework import serializers
from .models import Book, Author

#Serializer for the book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

#Serializer for the author model
#A nested serializer is used to implement the one to many relationship between an author and books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    
    class Meta:
        model = Author
        field = ['name']
    
    def validate(self, data):
        publication_year = data.get('publication_year')

        if publication_year > 2025:
            raise serializers.ValidationError("Publication year should not be set in the future")
        return data
