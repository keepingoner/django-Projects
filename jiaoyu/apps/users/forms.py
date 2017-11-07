from django import forms
from captcha.fields import CaptchaField



class Login_form(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5,error_messages={'invalid':'不能少于5位'})


class Register_form(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField()


class ForgetPwd_form(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()

class Reset_form(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)