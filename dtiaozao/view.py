#encoding: utf-8
from django.shortcuts import render_to_response,render
from account.models import LoginUser
from goodsIssue.models import GoodsReleased
from dtiaozao import function as fun

#新品上架展示
def index(request):
    allgoods = GoodsReleased.objects.all()
    goodsorder = []
    showgoods = set()
    for item in allgoods:
        if int(item.status) == 1:
            goodsorder += [item.id]
    goodsorder.sort()
    i = 1
    while i <= 4:
        try:
            showgoods.add(GoodsReleased.objects.get(id = goodsorder[-1*i]))
            i += 1
        except:break
    return render(request,'Base_Index.html',{"showgoods":showgoods},)
