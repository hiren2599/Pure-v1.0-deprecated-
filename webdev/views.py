from django.http import HttpResponse
from django.shortcuts import render

  # Create your views here.
def index(request):
    return render(request,'devnet/index.html')

def backdoorlogin(request):
    return render(request,'devnet/backdoorlogin.html')
