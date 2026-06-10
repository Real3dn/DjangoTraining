from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    name = request.GET.get('name') or 'user'
    return HttpResponse(f"Hello, {name}!")

def renderer(request):
    return render(request,'base.html')

def searcher(request):
    lala =  request.GET.get('search')
    return render(request,'searcher.html',{"lala":lala})