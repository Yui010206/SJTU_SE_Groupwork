#encoding: utf-8
from django.shortcuts import render,redirect
from form import getGoods
from goodsIssue.models import GoodsReleased
from account.models import LoginUser



#商品购买模块
def goodsPurchase(request):
    if not request.session.get('islogin'):
        msg = '你还未登陆，请先登陆！'
        return render(request,'error_msg.html', locals())

    if request.method == 'POST':
        data = request.POST
        buyer_id = request.session['user_info']['uid']
        condition = GoodsReleased.objects.get(id=data['good_id'])
        if condition.status ==1:
            condition.buyer=buyer_id
            condition.status=0
            condition.save()
            msg = '购买成功，请返回主页！'
        else:
            msg = '购买失败，已被人购买！'
    
        return render(request,'error_msg.html', locals())

#购买记录模块
def buyHistory(request):
    if not request.session.get('islogin'):
        msg = '你还没登录'
        return render(request,'error_msg.html',locals())
    #获取买家id
    buyer_id = request.session['user_info']['uid']
    bought_goods = {}
    bought_goods = getGoods(buyer_id,0)

    return render(request,'Good_BuyHistory.html',locals())

#购买记录中单品信息
def detail(request,good_id):
    if not request.session.get('islogin'):
        msg = '你还没登录'
        return render(request,'error_msg.html',locals())
    else:
        info = set()
        good = GoodsReleased.objects.get(id = good_id)
        buyer_name = request.session['user_info']['name']
        return render(request,"Good_BoughtDetail.html",locals())  

def saleHistory(request):
    if not request.session.get('islogin'):
        msg = '你还没登录'
        return render(request,'error_msg.html', locals())
    saler_id = request.session['user_info']['uid']
    all_goods = getGoods(saler_id,1)
    on_sale = []
    sold = []
    wait_ans = []
    for goods in all_goods:
        if goods.get('status') == 0:
            wait_ans.append(goods)
        elif goods.get('status') == 1:
            on_sale.append(goods)
        else :
            sold.append(goods)
    return render(request,'Good_Sale.html',locals())

#交易成功
def confirmation(request):
    if not request.session.get('islogin'):
        msg = '你还没登录'
        return render(request,'error_msg.html', locals())
    if request.method == "POST":
        data = request.POST
        good = GoodsReleased.objects.get(id = data['item_id'])
        good.status = 2
        good.save()
        return redirect('../trade/saleHistory')
        
#重新上架
def rerelease(request):
    if not request.session.get('islogin'):
        msg = '你还没登录'
        return render(request,'error_msg.html', locals())
    if request.method == "POST":
        data = request.POST
        good = GoodsReleased.objects.get(id = data['item_id'])
        good.status = 1
        good.save()
        return redirect('../trade/saleHistory')