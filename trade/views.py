#encoding: utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
import controlller
from dtiaozao import function as fun

def goodsList(req):
    if not req.session.get('islogin'):
        msg = 'Error'
        return render_to_response('error_msg.html', locals())
    saler_id = req.session['user_info']['uid']
    all_goods = controlller.getGoods(saler_id)
    on_sale = []
    saled = []
    wait_ans = []
    for goods in all_goods:
        print goods.get('status')
        if goods.get('status') == 0:
            wait_ans.append(goods)
        elif goods.get('status') == 1:
            on_sale.append(goods)
        else :
            saled.append(goods)
    return render_to_response('saler_page.html',locals())