from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View

from . import models
from . import forms


# Create your views here.

def empty_redirect(request):
    return HttpResponseRedirect(reverse_lazy('Apps.User:index'))


def index(request):
    return render(request, 'User/index.html', context={})


def login(request):
    return render(request, 'User/login.html', context={})


def signup(request):
    return render(request, 'User/signup.html', context={})


def info(request, uid):
    return HttpResponseRedirect(reverse_lazy('Apps.User:index'))


class LoginView(View):
    def __init__(self):
        super().__init__()
        self.ctx = {}

    def get(self, request):
        return render(request, 'User/login.html', context=self.ctx)

    def post(self, request):
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            check_result = self.__check(data["uid"], data["pwd"])
            if check_result == 1:
                self.__login(request, data["uid"])
            elif check_result == -1:
                pass
            elif check_result == 0:
                pass
        else:
            print('非法')
        return render(request, 'User/login.html', context=self.ctx)

    def __check(self, uid, pwd):
        u_obj = models.UserLogin.objects.filter(account=uid)
        if u_obj.exists():
            if u_obj.get().pwd == pwd:
                return 1
            else:  # pwd check failed
                self.ctx["check_result"] = "用户名或密码错误！"
                return -1
        else:
            self.ctx["check_result"] = "账号未注册！"
            return 0
        # 0 for not have this account 1 for check success -1 for check failed

    def __login(self, request, uid):
        request.session['is_login'] = True
        request.session['uid'] = uid
        self.ctx["msg"] = "登陆成功！"
        pass
