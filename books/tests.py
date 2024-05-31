from django.test import TestCase
from .models import Book, Author
from django.urls import reverse


class AuthorViewTests(TestCase):

    def setUp(self):
        self.author1 = Author.objects.create(name="Author One", bio="Bio for author one")
        self.author2 = Author.objects.create(name="Author Two", bio="Bio for author two")
        Book.objects.create(title="Book One", description="Description for book one", publication_date="2023-01-01", price=10.00)
        Book.objects.create(title="Book Two", description="Description for book two", publication_date="2023-01-02", price=15.00)


    def test_author_list_view(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author1.name)
        self.assertContains(response, self.author2.name)


    def test_author_detail_view(self):
        response = self.client.get(reverse('author_detail', args=[self.author1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author1.name)
        self.assertContains(response, self.author1.bio)


class BookViewTests(TestCase):

    def setUp(self):
        self.author1 = Author.objects.create(name="Author One", bio="Bio for author one")
        self.book1 = Book.objects.create(title="Book One", description="Description for book one", publication_date="2023-01-01", price=10.00)
        self.book2 = Book.objects.create(title="Book Two", description="Description for book two", publication_date="2023-01-02", price=15.00)
        self.book1.authors.add(self.author1)
        self.book2.authors.add(self.author1)

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book2.title)

    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book1.description)

