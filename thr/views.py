from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def thr1(request):
    return HttpResponse('This is Thirs String page')
def thr2(request):
    return render(request,'thr2.html')