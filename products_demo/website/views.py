from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    return HttpResponse("welcomee!!!!")

def home(request):
    return render(request,"website/Home.html")