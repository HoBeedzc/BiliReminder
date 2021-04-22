from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to BiliReminder!")


def yes(request):
    return HttpResponse("This is a test.")


def hello(request):
    return HttpResponse("Hello World!")
