# encoding: utf-8
from django.db import models
from django import forms

#用户模型及注册表
class LoginUser(models.Model):
    email = models.EmailField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=True)
    phone = models.BigIntegerField(blank = False)
    studentid = models.BigIntegerField(blank = False)
    address = models.CharField(max_length = 60,blank = False)

class LoginForm(forms.ModelForm):
    password = forms.CharField(label = "PassWord",widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Congfirm PassWord",widget = forms.PasswordInput)

    class Meta:
        model = LoginUser
        fields = ("email","password","phone","name","studentid","address")
    
