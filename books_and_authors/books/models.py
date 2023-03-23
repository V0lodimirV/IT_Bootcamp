from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.last_name}, {self.name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField(null=True)
    authors = models.ManyToManyField(Author)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return f"{self.title}, {self.publication_date}"
