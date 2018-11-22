#encoding: utf-8

from django.shortcuts import render_to_response,render
#from django.template import requestuestContext
from account.models import LoginUser
from goodsIssue.models import GoodsReleased
from dtiaozao import function as fun

#主页展示
def index(request):
    allgoods = GoodsReleased.objects.all()
    goodsorder = []
    showgoods = set()
    for item in allgoods:
        goodsorder += [item.id]
    goodsorder.sort()
    for i in range(1,5):
        try:
            showgoods.add(GoodsReleased.objects.get(id = goodsorder[-1*i]))
        except:break
    return render(request,'Base_Index.html',{"showgoods":showgoods},)



#搜索引擎模块
def search(request):
    if request.method == 'GET':
        msg = '非法访问！！！'
        return render_to_response('error_msg.html', locals())
    data = fun.warp_data(request.POST)
    goods_name = data['keywords']
    # goods_info = GoodsissueGoods.objects.filter(name__contains=goods_name)
    return render_to_response('goods_list.html', locals(), context_instance=requestuestContext(request))
