from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField('Author')
    summary = models.TextField(max_length=1000)
    genre = models.ManyToManyField('BookGenre')
    reading_status = models.ForeignKey('BookStatus', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class BookGenre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BookStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
