import pytest

from books.models import Author


@pytest.fixture
def authors():
    lst = []
    for x in range(10):
        lst.append(Author.objects.create(first_name=x, last_name=x))
    return lst
