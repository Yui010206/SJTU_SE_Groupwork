#encoding: utf-8
from django.shortcuts import render
from models import GoodsReleased,GoodsReleaseForm
from account.models import LoginUser
from dtiaozao import function as fun
import PIL

#新品发布
def release(request):
    if not request.session.get('islogin'):
        msg = '你还未登陆，请先登陆！'
        return render(request,'error_msg.html', locals())
    if request.method == "GET":
        releaseform = GoodsReleaseForm()
        return render(request,"Goods_Release.html",{"releaseform":releaseform})
    else:
        releaseform = GoodsReleaseForm(request.POST,request.FILES)
        if releaseform.is_valid():
            cd  = releaseform.cleaned_data
            uid = request.session['user_info']['uid'] # 获取用户ID
            new_good = releaseform.save(commit = False)
            new_good.saler_id = uid
            new_good.status = 1
            new_good.save()
            msg = "商品发布成功！"
            return render(request,"error_msg.html",locals())
        else:
            msg = "商品发布失败！"
            return render(request,"error_msg.html",locals())


#浏览市场
def market(request):
        allgoods = GoodsReleased.objects.filter(status=1)
        return render(request, "Good_Market.html",{"allgoods":allgoods},)
        
#查看详情
def detail(request,good_id):
    if not request.session.get('islogin'):
        msg = "你还未登陆，请先登陆！"
        return render(request,"error_msg.html",locals())
    else:
        info = set()
        good = GoodsReleased.objects.get(id = good_id)
        return render(request,"Good_Detail.html",{"good":good},)


#搜索模块
def search(request):
    if request.method == 'GET':
        return render(request,'search_test.html')
    else:
        data = fun.warp_data(request.POST)
        goods_name = data['keywords']
        goods_info = GoodsReleased.objects.filter(title__contains = goods_name)
        return render(request,'Good_Searched.html',locals(),) 



