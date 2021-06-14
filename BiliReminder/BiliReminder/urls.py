"""BiliReminder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Hello pages
    path('', views.empty_redirect),
    path('index/', views.index, name='index'),
    path('aboutus/', views.hello, name='aboutus'),
    path('yes/', views.yes, name='yes'),

    # global pages
    path('404/', views.HTTPStateCode404View.as_view(), name='404'),

    # admin urls
    path('admin/', admin.site.urls),

    # app urls
    path('user/', include('Apps.User.urls', namespace='User')),
    path('subscribe/', include('Apps.Subscribe.urls', namespace='Subscribe')),
    path('About/', include('Apps.About.urls',namespace='About')),
    path('Thanks/',include('Apps.Thanks.urls',namespace='Thanks')),
    path('Help/',include('Apps.Help.urls',namespace='Help')),

]
