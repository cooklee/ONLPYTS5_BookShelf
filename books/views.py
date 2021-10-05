from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from datetime import datetime

from books.forms import BookForm
from books.models import Author, Book


class IndexView(View):

    def get(self, request):
        response = render(request, 'base.html', )
        return response


class AuthorListView(View):

    def get(self, request):
        authors = Author.objects.all()
        response = render(request, 'author.html', {'authors': authors})
        return response


class BooksListView(View):

    def get(self, request):
        books = Book.objects.all()
        response = render(request, 'books.html', {'books': books, })
        return response


class AuthorAddView(View):

    def get(self, request):
        return render(request, 'add_author_form.html')

    def post(self, request):
        # a = {'first_name':'slawek',
        #  'last_name':'boguslawski'}
        # Author.objects.create(**a)->
        # Author.objects.create(first_name='slawek', last_name='boguslawski')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Author.objects.create(first_name=first_name, last_name=last_name)
        return redirect("authors_list_view")


class AddBookView(View):

    def get(self, request):
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            Book.objects.create(title=title, author=author)
            return redirect("books_list_view")
        return render(request, 'add_book.html', {'form': form})

