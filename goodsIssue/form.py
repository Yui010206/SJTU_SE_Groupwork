#encoding: utf-8
from account.models import LoginUser
from models import GoodsReleased
from django import forms
from dtiaozao import function as fun

# 商品发布的表单
class GoodsReleaseForm(forms.ModelForm):
    class Meta:
        model = GoodsReleased
        fields = ("title","detail","price","photo")

    

