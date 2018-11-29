#encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from account.models import LoginUser
from django import forms

class GoodsReleased(models.Model):
    saler =  models.ForeignKey(LoginUser,related_name = "goodsreleased")
    buyer = models.CharField(max_length = 100)  #记录买家
    title = models.CharField(max_length = 200)  # title是描述性的一句话，在商品列表中展示
    photo = models.ImageField(blank = False,upload_to = '.')
    photo2 = models.ImageField(blank = True,upload_to = '.')
    detail = models.TextField()                 # datail详细描述产品的各项参数，由卖家随意编写
    price = models.CharField(max_length = 100)
    status = models.IntegerField(default = 1)   #status表示物品的交易状态，1表示可交易，0表示交易中,2表示交易完成
    created = models.DateTimeField(default = timezone.now)  #发布信息时间
    updated = models.DateTimeField(auto_now=True)           #更新信息时间

    class Meta:
        ordering = ("title",)
        index_together = (('id','status'),)

    def __str__(self):
        return self.title

class GoodsReleaseForm(forms.ModelForm):
    class Meta:
        model = GoodsReleased
        fields = ("title","detail","price","photo")

