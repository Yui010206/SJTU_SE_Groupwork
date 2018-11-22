#encoding: utf-8
from account.models import LoginUser
from goodsIssue.models import GoodsReleased
from dtiaozao import function as fun

#获取商品信息（购买记录/销售）
def getGoods(user_id,p):
    result = []
    info = {}
    if p ==1: #卖家查询销售记录
        u = GoodsReleased.objects.filter(saler=user_id)
        if u:
            for re in u:
                info['title'] = re.title
                info['detail'] = re.detail
                info['photo'] = re.photo
                info['price'] = re.price
                info['status'] = re.status
                result.append(info)
                info = {}
        else:
            return []

    else:      #买家查询购买记录
        u = GoodsReleased.objects.filter(buyer=user_id)
        if u:
            for re in u:
                info['id'] = re.id
                info['title'] = re.title
                info['photo'] = re.photo
                info['status'] = re.status
                result.append(info)
                info = {}
        else:
            return []
    print result
    return result


