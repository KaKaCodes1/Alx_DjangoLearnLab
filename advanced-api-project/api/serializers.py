from rest_framework import serializers
from .models import Book, Author
from datetime import date

#Serializer for the book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    #When you are only validating one field use value rather than data as parameters
    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year should not be set in the future")
        return value

#Serializer for the author model
#A nested serializer is used to implement the one to many relationship between an author and books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        field = ['name','books']
    

