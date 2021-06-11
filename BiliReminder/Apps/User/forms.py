from django import forms


class LoginForm(forms.Form):
    uid = forms.CharField(required=True)
    pwd = forms.CharField(required=True)
