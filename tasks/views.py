from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse('Hello world!')

def taskList(request):
    return render(request, 'tasks/list.html')

def yourName(resquest, name):
    return render(resquest, 'tasks/yourname.html', {'name': name})