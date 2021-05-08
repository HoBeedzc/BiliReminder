from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

ctx = {
    'register_url': reverse_lazy('yes'),
    'hello_url': reverse_lazy('hello'),
    'index_url': reverse_lazy('index')
}


def empty_redirect(request):
    return HttpResponseRedirect('/index')


def index(request):
    return render(request, 'BiliReminder/index.html', context=ctx)


def yes(request):
    return render(request, "BiliReminder/test.html")


def hello(request):
    return render(request, "BiliReminder/hello.html", context=ctx)
