#encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
import form

#登录
def login(request):
    if request.method == 'GET':
       return render(request,"Account_Login.html")
    else:
        data = request.POST 
        rt = form.user_login(data)
        if rt == -1:
            msg = '账号或密码错误！'
        elif rt:
            #登录成功后，将用户信息添加到session中
            request.session['islogin'] = True
            user_info = {}
            user_info['uid'] = rt.id
            user_info['name'] = rt.name
            user_info['email'] = rt.email
            user_info['phone'] = rt.phone
            request.session['user_info'] = user_info
        else:
            msg = '账号或密码错误！'
        return render(request,'error_msg.html',locals())

#登出
def logout(request):
    if request.method == 'POST':
        msg = '非法访问！！'
        return render(request,'error_msg.html')
    else:
        #删除session信息
        del request.session['user_info']
        del request.session['islogin']
        return HttpResponseRedirect('/')


#注册
def register(request):
    if request.method == 'GET':
        status = False
        return render(request,'Accout_Register.html')
    else:
        status = True
        date = request.POST
        rt = form.user_register(date)
        if rt == 1:
          return HttpResponseRedirect('/')         #注册成功后自动跳转回首页但没有自动登录
        elif rt == 0:
            msg = '两次密码填写不正确！'
        elif rt == -2:
            msg = 'Email already exists!'
        elif rt == -3:
            msg = "Username already exists."
        else:
            msg = '注册失败，请联系站长！！！'
        return render(request,'Accout_Register.html')
