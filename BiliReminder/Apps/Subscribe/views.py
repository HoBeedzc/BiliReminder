from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Create your views here.

def empty_redirect(request):
    return HttpResponseRedirect(reverse_lazy('Apps.Subscribe:index'))


def index(request):
    return render(request, 'Subscribe/index.html', context={})
