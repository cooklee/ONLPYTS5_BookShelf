from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} autor: {self.author}"

class Publisher(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=50)
    nip = models.CharField(max_length=10)
    phone = models.IntegerField()
