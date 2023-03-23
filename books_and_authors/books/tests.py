from django.test import TestCase
from .models import Author, Book


class AuthorTestCase(TestCase):
    def test_create_author(self):
        author = Author.objects.create(name="0987654321")
        self.assertEqual(author.name, "0987654321")


class BookTestCase(TestCase):
    def test_create_book(self):
        book = Book.objects.create(title="1234567890")
        date = Book.objects.create(publication_date="1842-03-21")
        self.assertEqual(book.title, "1234567890")
        self.assertEqual(date.publication_date, "1842-03-21")
