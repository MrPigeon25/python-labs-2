from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  #  ИСПОЛЬЗУЕМ ПЕРВЫЙ ШАБЛОН

def hello(request):
    return render(request, 'static_handler.html')  #  ИСПОЛЬЗУЕМ ВТОРОЙ ШАБЛОН