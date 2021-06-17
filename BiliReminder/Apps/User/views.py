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
    return render(request, 'User/forget.html', context={})


def info(request):
    return render(request, 'User/info.html', context={})


def edit(request):
    return render(request, 'User/edit.html', context={})


def vip(request):
    return render(request, 'User/vip.html', context={})


class UserInfoView(View):
    def __init__(self):
        super().__init__()
        self.ctx = {}

    def get(self, request):
        return render(request, 'User/info.html', context=self.ctx)

    def post(self, request):
        return render(request, 'User/info.html', context=self.ctx)


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
                return HttpResponseRedirect(reverse_lazy('Subscribe:index'))
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


class LogoutView(View):
    def __init__(self):
        super().__init__()
        self.ctx = {}

    def get(self, request):
        if request.session.get('is_login', False):
            request.session['is_login'] = False
            request.session.clear()
        else:
            print('压根就没登陆')
        if int(request.GET.get('from')):
            return HttpResponseRedirect(reverse_lazy('Subscribe:index'))
        else:
            return HttpResponseRedirect(reverse_lazy('index'))


class LogoffView(View):
    def __init__(self):
        super().__init__()
        self.ctx = {}

    def get(self, request):
        if not request.session.get('is_login', False):
            return HttpResponseRedirect(reverse_lazy('User:login'))
        self.__get_user_info(request.session.get('uid'))
        if request.GET.get('confirm', False):
            self.ctx['confirm'] = 1
        else:
            pass
        return render(request, 'User/logoff.html', context=self.ctx)

    def post(self, request):
        if not request.session.get('is_login', False):
            return HttpResponseRedirect(reverse_lazy('User:login'))
        self.__get_user_info(request.session.get('uid'))
        logoff_obj = forms.LogoffForm(request.POST)
        if logoff_obj.is_valid():
            data = logoff_obj.cleaned_data
            acc = request.session.get('uemail')
            user_obj = models.UserLogin.objects.filter(account=acc).get()
            if user_obj.pwd == data['pwd']:
                self.__del_account(acc)
                if request.session.get('is_login', False):
                    request.session['is_login'] = False
                    request.session.clear()
            else:
                self.ctx['msg'] = "密码核验失败！"
                self.ctx['confirm'] = 1
        else:
            self.ctx['msg'] = "输入数据不合法！"
            self.ctx['confirm'] = 1
        return render(request, 'User/logoff.html', context=self.ctx)

    def __get_user_info(self, uid):
        user_obj = models.User.objects.get(uid=uid)
        self.ctx['name'] = user_obj.name
        if user_obj.tel:
            self.ctx['tel'] = user_obj.tel
        else:
            self.ctx['tel'] = '暂未绑定'
        self.ctx['email'] = user_obj.email
        if user_obj.bili_uid:
            self.ctx['bili_uid'] = user_obj.bili_uid
        else:
            self.ctx['bili_uid'] = '暂未绑定'

    def __del_account(self, acc):
        user_obj = models.UserLogin.objects.get(account=acc)
        user = user_obj.user
        user_obj.delete()
        user.delete()
        self.ctx['confirm'] = 2


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
