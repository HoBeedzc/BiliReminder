from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View

from . import models
from . import forms


# Create your views here.
def empty_redirect(request):
    return HttpResponseRedirect(reverse_lazy('Apps.About:index'))


def index(request):
    return render(request, 'About/index.html', context={})

# Create your views here.
