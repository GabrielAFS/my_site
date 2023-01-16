from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>POSTS</h1>")

def post_detail(request, slug):
    return HttpResponse(f"<h1>POST {slug}</h1>")
