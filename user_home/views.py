from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, "home/index.html")
def contact(requests):
    return render(requests, "home/contact.html")