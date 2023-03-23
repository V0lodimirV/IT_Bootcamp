from django.contrib import admin
from .models import Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "name", "email")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publication_date")
