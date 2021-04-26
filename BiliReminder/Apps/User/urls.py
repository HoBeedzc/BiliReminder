from django.urls import path
from . import views

app_name = 'Apps.User'

urlpatterns = [
    path('', views.empty_redirect),
    path('index/', views.index, name='index'),


]