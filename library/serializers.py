from rest_framework import serializers
from .models import Library, Book

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('name', 'description')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'library_id')
