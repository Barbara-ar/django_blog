from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, default="Unknown Author")  # Agregar valor predeterminado
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
