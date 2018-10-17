#encoding: utf-8
__author__ = 'SE_Group'

from django.shortcuts import render
from login.models import LoginUser, GoodsissueGoods, GoodsissueIssuer, GoodsissueSaler
from dtiaozao import function as fun

#主页
def index(req):
    #获得数据库中的数据，全表扫描
    users = LoginUser.objects.all()
    goodses = GoodsissueGoods.objects.all()
    issuers = GoodsissueIssuer.objects.all()
    salers = GoodsissueSaler.objects.all()
    return render(req,'index.html',locals())


#搜索引擎模块
def search(req):
    if req.method == 'GET':
        msg = '非法访问！！！'
        return render(req,'error_msg.html', locals())
    data = fun.warp_data(req.POST)
    goods_name = data['keywords']
    goods_info = GoodsissueGoods.objects.filter(name__contains=goods_name)
    return render(req,'goods_list.html',locals())
