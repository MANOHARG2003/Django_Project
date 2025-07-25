from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse("<h1>Welcome to the home page</h1>")
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")