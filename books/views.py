from django.shortcuts import render,  get_object_or_404
from .models import Book, Author
from django.db.models import Count


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

