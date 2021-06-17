from django import forms


class LoginForm(forms.Form):
    uid = forms.CharField(required=True)
    pwd = forms.CharField(required=True)


class SignupForm(forms.Form):
    email = forms.CharField(required=True)
    name = forms.CharField(required=True)
    pwd = forms.CharField(required=True)
    pwd2 = forms.CharField(required=True)


class LogoffForm(forms.Form):
    pwd = forms.CharField(required=True)
