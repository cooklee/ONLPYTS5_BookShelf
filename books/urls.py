"""bookshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from books import views

urlpatterns = [
    path('books/', views.BooksListView.as_view(), name='books_list_view'),
    path('book/<int:pk>/', views.DetailBookView.as_view(), name='detail_book_view'),
    path('authors/', views.AuthorListView.as_view(), name='authors_list_view'),
    path('publisher/', views.PublisherListView.as_view(), name='publisher_list_view'),
    path('add_author/', views.AuthorAddView.as_view(), name='authors_add_view'),
    path('add_book/', views.AddBookView.as_view(), name='book_add_view'),
    path('add_publisher/', views.AddPublisherView.as_view(), name='publisher_add_view'),
    path('add_booksonloan/', views.AddBooksOnLoanView.as_view(), name='booksonloan_add_view'),
    path('my_booksonloan/', views.MyBooksOnLoanView.as_view(), name='my_booksonloan_add_view'),
    path('author/<int:pk>/', views.DetailAuthorView.as_view(), name='detail_author_view'),
    path('publisher/<int:pk>/', views.UpdatePublisherView.as_view(), name='update_publisher_view'),
    path('delete_author/<int:pk>/', views.DeleteAuthorView.as_view(), name='delete_author_view'),
    path('delete_book/<int:pk>/', views.DeleteBookView.as_view(), name='delete_book_view'),
]
