from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from datetime import datetime

from books.forms import BookForm, AuthorForm, PublisherModelForm, BooksOnLoanModelForm
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
        form = AuthorForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author.objects.create(**form.cleaned_data)
            return redirect("authors_list_view")
        return render(request, 'form.html', {'form': form})


class AddBookView(View):

    def get(self, request):
        form = BookForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            Book.objects.create(title=title, author=author)
            return redirect("books_list_view")
        return render(request, 'form.html', {'form': form})

class AddPublisherView(View):

    def get(self, request):
        form = PublisherModelForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = PublisherModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Udało dodać sie publishera")
        return render(request, 'form.html', {'form': form})


class AddBooksOnLoanView(View):

    def get(self, request):
        form = BooksOnLoanModelForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = BooksOnLoanModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Udało dodać sie BooksOnLoan")
        return render(request, 'form.html', {'form': form})

