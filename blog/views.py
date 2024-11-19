from django.shortcuts import render

from django.http import HttpResponse

def HelloWord(request):
    return HttpResponse('<H1>Hello Word<H1>')
