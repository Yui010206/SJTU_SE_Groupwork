#encoding: utf-8

from __future__ import unicode_literals

from django.db import models

#商品表
class GoodsissueGoods(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    owner = models.ForeignKey('LoginUser', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    size = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=255, blank=True)
    introduction = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(blank=True, null=True)
    imagefile = models.CharField(max_length=255, blank=True)
    status = models.IntegerField(blank=True,default=1)

    class Meta:
        db_table = 'goodsissue_goods'


#商品发布表
class GoodsissueIssuer(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    uid = models.ForeignKey('LoginUser', db_column='uid', blank=True, null=True)
    goods = models.ForeignKey(GoodsissueGoods, blank=True, null=True)
    issuedate = models.DateTimeField(db_column='issueDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'goodsissue_issuer'


#商品销售表
class GoodsissueSaler(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    buyer = models.ForeignKey('LoginUser', blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    tradedate = models.DateTimeField(db_column='tradeDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'goodsissue_saler'
        
#用户表
class LoginUser(models.Model):
    id = models.AutoField(primary_key=True)  
    email = models.CharField(max_length=255, blank=True)
    passwd = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'login_user'

