from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render (request, 'blog/home.html')
def contact(request):
    return HttpResponse ('<h2>contact vash syca</h2>')
# Create your views here.
