from django.shortcuts import render

def post_List(request):
    return render(request,"posts/posts_List.html")
# Create your views here.
def contact(request):
    return render(request,'posts/i.html')
