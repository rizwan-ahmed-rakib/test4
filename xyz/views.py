from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse(
        "<h1>assalamualaikum wa rahmatullahi --4000-<br>it is p4 home<h1><a href='/xyz/customer/'>contact</a> ")


def contact(request):
    return HttpResponse(
        "<h1>assalamualaikum wa rahmatullahi --contact777-<br>it is p4 customer contact<h1><a href='/xyz/home/'>back</a>")


def homepage(request):
    return render(request, 'xyz_app/index.html')


def second(request):
    return render(request, 'xyz_app/second.html')


def test(request):
    return render(request, "xyz_app/test.html")
