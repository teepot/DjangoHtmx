from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag_name


class Author(models.Model):
    name = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number_of_pages = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title
