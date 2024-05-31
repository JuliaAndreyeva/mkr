from django.shortcuts import render,  get_object_or_404
from .models import Book, Author
from django.db.models import Count


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_detail.html', {'book': book})
