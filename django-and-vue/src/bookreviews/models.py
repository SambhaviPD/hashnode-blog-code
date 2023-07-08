from django.db import models

# Create your models here.
class BookReview(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    review = models.TextField()