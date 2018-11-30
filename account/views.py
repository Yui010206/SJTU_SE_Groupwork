#encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect

from models import LoginUser,LoginForm
from dtiaozao import function as fun


#登录
def login(request):
    if request.method == 'GET':
       return render(request,"Account_Login.html")
    else:

        cd = request.POST
        encriped=fun.mk_md5(cd.get("password"))
        email = cd.get("email")
        try:
            user = LoginUser.objects.get(email = email)
        except:
            msg = "账号不存在 ！"
            return render(request,"error_msg.html",locals())

        if user.password != encriped :
            msg = "密码或账号不正确"

        if user.password == encriped :
            request.session['islogin'] = True
            user_info = {}
            user_info['uid'] = user.id
            user_info['name'] = user.name
            user_info['email'] = user.email
            user_info['phone'] = user.phone
            request.session['user_info'] = user_info
            msg = '登陆成功'

        return render(request,"error_msg.html",locals())


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
        regform = LoginForm()
        return render(request,'Accout_Register.html',{"regform":regform})
    else:
        cd = request.POST
        print cd
        regform = LoginForm(request.POST)
        if regform.is_valid():
            new_user = regform.save(commit = False)
            passwd = fun.mk_md5(cd['password'])
            new_user.password = passwd
            exisitusers = LoginUser.objects.all()
            #错误提示：
            try:
                if LoginUser.objects.get(email = cd["email"]):
                    errorem = set()
                    errorem.add("该邮箱已被注册")
                    return render(request,'Accout_Register.html',{"regform":regform,"errorem":errorem,})
            except:
                pass

            if cd["password"] != cd['password2']:
                errorpwd2 = set()
                errorpwd2.add("两次密码不相同")
                return render(request,'Accout_Register.html',{"regform":regform,"errorpwd2":errorpwd2,})

            if int(cd["phone"]) < 13000000000 or int(cd["phone"]) > 19999999999:
                errortel = set()
                errortel.add("号码格式不正确")
                return render(request,'Accout_Register.html',{"regform":regform,"errortel":errortel,})

            try:
                if LoginUser.objects.get(phone = cd["phone"]):
                    errortel = set()
                    errortel.add("该手机已被注册")
                    return render(request,'Accout_Register.html',{"regform":regform,"errortel":errortel,})
            except:
                pass


            if int(cd["studentid"]) <= 513000000000 or int(cd["studentid"]) >= 518100000000:
                errorid = set()
                errorid.add("学号格式不正确")
                return render(request,'Accout_Register.html',{"regform":regform,"errorid":errorid,})
                
            try:
                if LoginUser.objects.get(studentid = cd["studentid"]):
                    errorid = set()
                    errorid.add("该学号已被注册")
                    return render(request,'Accout_Register.html',{"regform":regform,"errorid":errorid,})
            except:
                pass

            try:
                if LoginUser.objects.get(name = cd["name"]):
                    errornm = set()
                    errornm.add("该用户名已被注册")
                    return render(request,'Accout_Register.html',{"regform":regform,"errornm":errornm,})
            except:
                pass

            new_user.save()
            #自动登陆
            user = LoginUser.objects.get(email = cd["email"])
            request.session['islogin'] = True
            user_info = {}
            user_info['uid'] = user.id
            user_info['name'] = user.name
            user_info['email'] = user.email
            user_info['phone'] = user.phone
            request.session['user_info'] = user_info

            return HttpResponseRedirect('/')
        else:
            if cd["password"] == '':
                errorpwd = set()
                errorpwd.add("密码不能为空")
                return render(request,'Accout_Register.html',{"regform":regform,"errorpwd":errorpwd,})
            if cd["password2"] == '':
                errorpwd2 = set()
                errorpwd2.add("确认密码不能为空")
                return render(request,'Accout_Register.html',{"regform":regform,"errorpwd2":errorpwd2,})
            if cd["name"] == '':
                errornm = set()
                errornm.add("用户名不能为空")
                return render(request,'Accout_Register.html',{"regform":regform,"errornm":errornm,})
            if cd["phone"] == '':
                errortel = set()
                errortel.add("手机不能为空")
                return render(request,'Accout_Register.html',{"regform":regform,"errortel":errortel,})
            if cd["studentid"] == '':
                errorid = set()
                errorid.add("学号不能为空")
                return render(request,'Accout_Register.html',{"regform":regform,"errorid":errorid,})
            if cd["address"] == '':
                errorad = set()
                errorad.add("住址不能为空")
                return render(request,'Accout_Register.html',{"regform":regform,"errorad":errorad,})
            else :
                msg = '注册失败，请重新注册！'
                return render(request,"error_msg.html",locals())
