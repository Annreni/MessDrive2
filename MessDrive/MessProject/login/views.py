import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello World")
def test(request):
     return render(request, 'test.html')
def inmate(request):
    return render(request, 'inmate.html')
