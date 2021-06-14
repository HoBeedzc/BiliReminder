from django.urls import path
from . import views

app_name = 'Apps.User'

urlpatterns = [
    path('', views.empty_redirect),
    path('index/', views.index, name='index'),
    path('info/<int:uid>', views.info, name='info'),
    path('edit/',views.edit, name='edit'),
    path('vip/',views.vip, name='vip'),
    path('logoff/',views.logoff, name='logoff'),

    
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('forget/', views.forget, name="forget"),

]
