from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Welcome to BiliReminder!")


def yes(request):
    return render(request, "BiliReminder/test.html")


def hello(request):
    return HttpResponse("Hello World!")
