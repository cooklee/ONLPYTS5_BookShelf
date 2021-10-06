from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('detail_author_view', args=(self.pk, ))

    def get_delete_url(self):
        return reverse('delete_author_view', args=(self.pk, ))


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail_book_view', args=(self.pk, ))

    def get_delete_url(self):
        return reverse('delete_book_view', args=(self.pk, ))

    def __str__(self):
        return f"{self.title} autor: {self.author}"

def validator_name(val):
    if len(val) < 3:
        raise ValidationError("Za ....")

class Publisher(models.Model):
    name = models.CharField(max_length=128, validators=[validator_name])
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=50)
    nip = models.CharField(max_length=10)
    phone = models.IntegerField()

class BooksOnLoan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    when = models.DateField(auto_now=True)


