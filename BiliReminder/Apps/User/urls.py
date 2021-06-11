from django.urls import path
from . import views

app_name = 'Apps.User'

urlpatterns = [
    path('', views.empty_redirect),
    path('index/', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('info/<int:uid>', views.info, name='info'),

]
