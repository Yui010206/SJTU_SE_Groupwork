#encoding: utf-8
from account.models import LoginUser
from goodsIssue.models import GoodsReleased
from dtiaozao import function as fun

def getGoods(user_id,saler):
    result = []
    info = {}
    if saler :
        u = GoodsReleased.objects.filter(saler_id=user_id)
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
    return result