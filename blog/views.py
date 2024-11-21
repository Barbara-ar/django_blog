from django.http import HttpResponse

def HelloWord(request):
    return HttpResponse('<h1>Hello World</h1>')  # Etiquetas correctamente cerradas
