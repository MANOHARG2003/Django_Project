from django.shortcuts import render

# Create your views here.
def Env(request):
    return render(request,"environment/index.html")