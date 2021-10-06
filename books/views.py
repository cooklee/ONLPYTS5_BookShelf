
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from datetime import datetime

from django.views.generic import ListView, CreateView

from books.forms import BookForm, AuthorForm, PublisherModelForm, BooksOnLoanModelForm, LoginForm, AuthorModelForm
from books.models import Author, Book, BooksOnLoan


class IndexView(View):

    def get(self, request):
        response = render(request, 'base.html', )
        return response


class AuthorListView(ListView):
    model = Author
    template_name = 'author.html'

    # def get(self, request):
    #     authors = Author.objects.all()
    #     response = render(request, 'author.html', {'authors': authors})
    #     return response


class BooksListView(View):

    def get(self, request):
        books = Book.objects.all()
        response = render(request, 'books.html', {'books': books, })
        return response


class AuthorAddView(CreateView):
    model = Author
    template_name = 'form.html'
    success_url = reverse_lazy('authors_add_view')
    form_class = AuthorModelForm
    # def get(self, request):
    #     form = AuthorForm()
    #     return render(request, 'form.html', {'form': form})
    #
    # def post(self, request):
    #     form = AuthorForm(request.POST)
    #     if form.is_valid():
    #         Author.objects.create(**form.cleaned_data)
    #         return redirect("authors_list_view")
    #     return render(request, 'form.html', {'form': form})


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
            books_on_loan = form.save(commit=False)
            books_on_loan.user = request.user
            books_on_loan.save()
            form.save_m2m()
            return HttpResponse("Udało dodać sie BooksOnLoan")
        return render(request, 'form.html', {'form': form})

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return HttpResponse("Udało sie zalogować")
            else:
                return HttpResponse("Błędne dane logowania")
        return render(request, 'form.html', {'form': form})


class MyBooksOnLoanView(View):

    def get(self, request):
        booksOnLoan = BooksOnLoan.objects.filter(user=request.user)
        return render(request, 'Myloans.html', {'loans':booksOnLoan})


class DetailAuthorView(View):
    def  get(self, request, id):
        author = Author.objects.get(pk=id)
        return render(request, 'detail_author.html', {'author':author})