from django.urls import path
from . import views

app_name = 'Apps.About'

urlpatterns = [
    path('', views.empty_redirect, name='empty'),
    path('index/', views.index, name='index'),
]