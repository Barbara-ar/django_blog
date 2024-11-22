from django.http import HttpResponse

def list_books(request):
    return HttpResponse("List of books")

def create_book(request):
    return HttpResponse("Create a book")

def update_book(request, book_id):
    return HttpResponse(f"Update book {book_id}")

def delete_book(request, book_id):
    return HttpResponse(f"Delete book {book_id}")
