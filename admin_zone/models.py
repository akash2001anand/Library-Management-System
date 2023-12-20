from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=250)
    mobno = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_pages = models.PositiveIntegerField()
    def __str__(self):
        return self.book_title