import pytest
from django.contrib.auth.models import User

from books.models import Author, Book


@pytest.fixture
def authors():
    lst = []
    for x in range(10):
        lst.append(Author.objects.create(first_name=x, last_name=x))
    return lst


@pytest.fixture
def books(authors):
    lst = []
    for x in range(10):
        lst.append(Book.objects.create(title=x, author_id=authors[0].id))
    return lst

@pytest.fixture
def user():
    return User.objects.create(username='cooklee')

