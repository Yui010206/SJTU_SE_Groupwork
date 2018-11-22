#encoding: utf-8
from django.shortcuts import render
from form import GoodsReleaseForm
from models import GoodsReleased
from account.models import LoginUser
import PIL

# 商品发布
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
            new_good.satus = 1
            new_good.save()
            msg = "商品发布成功！"
            return render(request,"error_msg.html",locals())
        else:
            msg = "商品发布失败！"
            return render(request,"error_msg.html",locals())


#浏览市场模块
def market(request):
        allgoods = GoodsReleased.objects.filter(status=1)
        return render(request, "Good_Market.html",{"allgoods":allgoods},)
        
#请求购买
def detail(request,good_id):
    if not request.session.get('islogin'):
        msg = "你还未登陆，请先登陆！"
        return render(request,"error_msg.html",locals())
    else:
        info = set()
        good = GoodsReleased.objects.get(id = good_id)
        return render(request,"Good_Detail.html",{"good":good},)    

