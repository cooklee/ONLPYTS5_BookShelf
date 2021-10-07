import pytest
from django.test import TestCase, Client
# Create your tests here.
from django.urls import reverse


def test_empty():
    client = Client() #tworze clienta który bedzie udawał przeglądarke
    response = client.get(reverse("index_view")) #wchodze na podany adres metodą get
    assert response.status_code == 200 #sprawdzam czy odpowiedz jest 200

def test_empty_post():
    client = Client()
    response = client.post(reverse("index_view"))
    assert response.status_code == 405

@pytest.mark.django_db
def test_author_list_get():
    client = Client()
    response = client.get(reverse("authors_list_view"))
    assert response.status_code == 200
    authors_list = response.context['object_list']
    assert authors_list.count() == 0

@pytest.mark.django_db
def test_author_list_get_not_empty(authors):
    client = Client()
    response = client.get(reverse("authors_list_view"))
    assert response.status_code == 200
    authors_list = response.context['object_list']
    assert authors_list.count() == len(authors)
    for author in authors:
        assert  author in authors_list

@pytest.mark.django_db
def test_books_list_get_not_empty(books):
    client = Client()
    response = client.get(reverse("books_list_view"))
    assert response.status_code == 200
    books_list = response.context['object_list']
    assert books_list.count() == len(books)
    for book in books:
        assert  book in books_list


@pytest.mark.django_db
def test_add_author_get_not_login():
    client = Client()
    response = client.get(reverse("authors_add_view"))
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_author_get_login(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("authors_add_view"))
    assert response.status_code == 200


