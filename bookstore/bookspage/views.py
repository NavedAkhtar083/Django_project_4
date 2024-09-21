from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'bookspage/index.html')

def about(request):
    return HttpResponse("hello ia am about page ")

def home(request):
    return HttpResponse("hello ia am Home page ")

def contact(request):
    return HttpResponse("hello ia am contact page ")

def tracker(request):
    return HttpResponse("hello ia am tracker page ")