from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sec1(request):
    return HttpResponse('It is second string sentence')

def sec2(request):
    return render(request,'sec2.html')