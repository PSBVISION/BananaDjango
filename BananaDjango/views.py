from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("<h1>Home</h1>")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("<h2>About</h2>")

def contact(request):
    return HttpResponse("<h3>Contact</h3>")