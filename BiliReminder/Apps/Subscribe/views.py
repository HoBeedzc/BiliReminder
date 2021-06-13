from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View

from . import models
from . import forms


# Create your views here.

def empty_redirect(request):
    return HttpResponseRedirect(reverse_lazy('Apps.Subscribe:index'))


def index(request):
    return render(request, 'Subscribe/index.html', context={})


class IndexView(View):
    def __init__(self):
        super(IndexView, self).__init__()
        self.ctx = {}

    def get(self, request):
        return render(request, 'Subscribe/index.html', context=self.ctx)

