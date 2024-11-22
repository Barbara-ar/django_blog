# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='home'),  # Página principal que lista los libros
    path('create/', views.create_book, name='create_book'),  # Crear un nuevo libro
    path('update/<int:book_id>/', views.update_book, name='update_book'),  # Actualizar un libro específico
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),  # Eliminar un libro específico
]
