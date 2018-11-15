#encoding: utf-8
from account.models import LoginUser
from dtiaozao import function as fun


#用户注册处理
def user_register(data):
    condition = fun.warp_data(data)

    #change start

    if LoginUser.objects.filter(email=condition['email']):
    	return -2
    if LoginUser.objects.filter(name=condition['name']):
    	return -3
    #change end

    if condition['passwd'] != condition['repasswd']:
        return 0
    del condition['repasswd']
    passwd = fun.mk_md5(condition['passwd'])
    condition['passwd'] = passwd
    #数据库的存储
    u = LoginUser(**condition)
    u.save()
    if u.name:
        return 1
    else:
        return -1

#用户登录处理
def user_login(data):
    condition = fun.warp_data(data)
    email = condition['email']
    if not LoginUser.objects.filter(email=condition['email']):
    	return -1
    r = LoginUser.objects.get(email=email)
    passwd = fun.mk_md5(condition['passwd'])  
    # 判断数据库的账号匹配结果是否存在以及密码是否匹配
    if not r or passwd != r.passwd:
        r = {}
    return r