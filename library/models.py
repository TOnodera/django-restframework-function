from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    published = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title
