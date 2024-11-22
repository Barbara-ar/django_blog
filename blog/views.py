# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from item.models import Book

def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title', 'Nuevo Libro')
        description = request.POST.get('description', 'Descripción del libro')
        book = Book.objects.create(title=title, description=description)
        return JsonResponse({'message': f'Libro creado: {book.title}'})

def list_books(request):
    books = Book.objects.all().values()
    return JsonResponse({'books': list(books)})

def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.description = request.POST.get('description', book.description)
        book.save()
        return JsonResponse({'message': f'Libro actualizado: {book.title}'})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return JsonResponse({'message': 'Libro eliminado'})
