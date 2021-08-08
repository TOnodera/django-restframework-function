from rest_framework import serializers
from .models import Book

class BookSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Book
        verbose_name = "book"