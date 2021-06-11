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


def forget(request):
    return render(request, 'User/signup.html', context={})


def info(request, uid):
    return HttpResponseRedirect(reverse_lazy('Apps.User:index'))


class LoginView(View):
    def __init__(self):
        super().__init__()
        self.ctx = {}

    def get(self, request):
        if request.session.get('is_login', False):
            cnt_uid = request.session.get('uemail')
            self.ctx["msg"] = "当前已登陆账号：{}，请勿重复登陆！".format(cnt_uid)
        return render(request, 'User/login.html', context=self.ctx)

    def post(self, request):
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            check_result = self.__check(data["uid"], data["pwd"])
            if check_result == 1:
                self.__login(request, data["uid"])
                return HttpResponseRedirect(reverse_lazy('index'))
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

    def __login(self, request, email):
        user_obj = models.UserLogin.objects.get(account=email)
        request.session['is_login'] = True
        request.session['uid'] = user_obj.user.uid
        request.session['uname'] = user_obj.user.name
        request.session['uemail'] = user_obj.account
        self.ctx["msg"] = "登陆成功！"
        pass


class SignupView(View):
    def __init__(self):
        super().__init__()
        self.ctx = {}

    def get(self, request):
        if request.session.get('is_login', False):
            cnt_uid = request.session.get('uemail')
            self.ctx["msg"] = "当前已登陆账号：{}，如需注册新账号请先退出登陆！".format(cnt_uid)
        return render(request, 'User/signup.html', context=self.ctx)

    def post(self, request):
        signup_form = forms.SignupForm(request.POST)
        if signup_form.is_valid():
            data = signup_form.cleaned_data
            if self.__check(data["email"]):  # 验证是否有重复注册
                new_user = models.User()
                new_user.name = data["name"]
                new_user.email = data["email"]
                new_user.save()

                new_user_login = models.UserLogin()
                new_user_login.account = data["email"]
                new_user_login.pwd = data["pwd"]
                new_user_login.user = new_user
                new_user_login.save()

                # 注册成功
                return HttpResponseRedirect(reverse_lazy('User:login'))
            else:
                pass
        else:
            self.ctx["msg"] = "表单填写不合法！"
        return render(request, 'User/signup.html', context=self.ctx)

    def __check(self, email):
        res = models.UserLogin.objects.filter(account=email).exists()
        if res:
            self.ctx["check"] = "该账号已被注册！"
            return 0
        else:
            return 1
