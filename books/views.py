from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from datetime import datetime

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from books.forms import BookForm, PublisherModelForm, BooksOnLoanModelForm, AuthorModelForm
from books.models import Author, Book, BooksOnLoan, Publisher

from django.contrib import messages


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

class DetailBookView(DetailView):
    model = Book
    template_name = 'detail_book.html'




class AuthorAddView(CreateView):
    model = Author
    template_name = 'form.html'
    # success_url = reverse_lazy('authors_add_view')
    form_class = AuthorModelForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, 'Udało się')
        return super().form_valid(form)
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


class AddBookView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

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






class MyBooksOnLoanView(View):

    def get(self, request):
        booksOnLoan = BooksOnLoan.objects.filter(user=request.user)
        return render(request, 'Myloans.html', {'loans': booksOnLoan})


class DetailAuthorView(DetailView):
    model = Author
    template_name = 'detail_author.html'


class UpdatePublisherView(UpdateView):
    model = Publisher
    template_name = 'form.html'
    fields = '__all__'
    success_url = "/"

    # def  get(self, request, id):
    #     author = Author.objects.get(pk=id)
    #     return render(request, 'detail_author.html', {'author':author})
class DeleteAuthorView(DeleteView):
    model = Author
    success_url = '/'
    template_name = 'form.html'

class DeleteBookView(DeleteView):
    model = Book
    success_url = '/'
    template_name = 'form.html'
