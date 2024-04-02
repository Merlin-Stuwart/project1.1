from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fir1(request):
    return HttpResponse('This is FIR ONE')

def fir2(request):
    return render(request,'fir2.html')