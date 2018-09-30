from django.views import generic

from books.models import Book


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book
