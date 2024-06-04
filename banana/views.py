from django.shortcuts import render

# Create your views here.
def all_bananas(request):
    return render(request, 'banana/all_bananas.html')