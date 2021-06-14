from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View

ctx = {}

def empty_redirect(request):
    return HttpResponseRedirect('/index')


def index(request):
    return render(request, 'BiliReminder/index.html', context=ctx)


def yes(request):
    return render(request, "BiliReminder/test.html")


def hello(request):
    return render(request, "BiliReminder/hello.html", context=ctx)


class HTTPStateCode404View(View):
    def __init__(self):
        super(HTTPStateCode404View, self).__init__()
        self.ctx = {}

    def get(self, request):
        return render(request, "BiliReminder/404.html", context=self.ctx)
