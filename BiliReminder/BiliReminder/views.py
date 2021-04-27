from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy


def empty_redirect(request):
    return HttpResponseRedirect('/index')


def index(request):
    return render(request, 'BiliReminder/index.html')


def yes(request):
    return render(request, "BiliReminder/test.html")


def hello(request):
    return render(request, "BiliReminder/hello.html")
