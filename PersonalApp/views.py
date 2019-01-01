from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'content': ['if you want to contact me, please email', 'syedfakhar25@gmail.com','+923009169564']})