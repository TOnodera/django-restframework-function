from django.contrib import admin
from .models import Book, Library

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)
