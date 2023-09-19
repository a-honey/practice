from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  return HttpResponse('Hello:D')

def hello(request, id):
  return HttpResponse('안녕하세요, ' + id + '님!')