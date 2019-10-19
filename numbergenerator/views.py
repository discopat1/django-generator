from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('this is homepage')
    return render(request, 'homepage.html')