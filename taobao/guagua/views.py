# coding=UTF-8
import base64
from random import randint
from django.shortcuts import render
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

import top as taobao
import top.api as topapi
# next for online app
#taobao.setDefaultAppInfo("21446815", "5e8279097b48bd0eefcec5f48c7381eb")
# next for sandbox test
taobao.setDefaultAppInfo("1021446815", "sandbox97b48bd0eefcec5f48c7381eb")

# top(): 用于获取数据的函数接口
# 参数： 1. api_name: 需要调用的函数名称； 2. kwarg: 需要传入的参数; 3.sessionkey: 作为关键字参数传入sessionkey，如果没有该关键字则表示不使用sessionkey
# 返回值： 正常返回json格式的数据，发生错误时返回异常
# 例子： top('UserGetRequest', fields='nick, sex', sessionkey='xxxx') 
def top(api_name, **kwarg):
    api_name = api_name + 'Request'
    if hasattr(topapi, api_name):
        api = getattr(topapi, api_name)
    else:
        raise ImportError('no api %s found' % aip_name)
    # 测试用
    a = api("gw.api.tbsandbox.com")
    #sdbsessionkey = '6101f23c7a9a2e8d90b4c74fbfd2bc21283630269ab37d42066555142' #user: sandbox_seller_0
    #sdbsessionkey = '6100c248a74c1e577ca89bd9b89f574a18a8f16a31452282076226627' # user: sandbox_b_20
    # 上线环境用 
    # a = api()
    authrize = None
    while kwarg:
        key, value = kwarg.popitem()
        if hasattr(a, key):
            setattr(a, key, value)
        else:
            if key is 'sessionkey':
                authrize = value
            elif key is not 'sessionkey':
                raise AttributeError('some attributes do not exist!')    
    return a.getResponse(authrize)

def test(api_name, id, **kwarg):
    if kwarg.get('sessionkey', 0) is 1:
        sessionkey = User.objects.get(id=id).userprofile.sessionkey
        kwarg.update({'sessionkey': sessionkey})
        res = top(api_name, **kwarg)
    else:
        res = top(api_name, **kwarg)
    return res
    
def fetchuserinfo(request):
    if request.method == 'GET':
        get = request.GET.copy()
        if get.has_key('top_session'):
            sessionkey = get['top_session']
        if get.has_key('top_parameters'):
            para_str = base64.b64decode(get['top_parameters'])
            para_dict = dict([item.split('=') for item in para_str.split('&')])

        user = User.objects.create_user(para_dict['visitor_nick'], password=para_dict['visitor_nick'])
        profile = user.get_profile()
        profile.taobao_id = para_dict['visitor_id']
        profile.taobao_nick = para_dict['visitor_nick']
        profile.sessionkey = sessionkey
        profile.start_date = user.date_joined
        profile.save()
        user = authenticate(username = para_dict['visitor_nick'], password = para_dict['visitor_nick'])
        login(request, user)
        #login(request, user)
    return HttpResponseRedirect('/pwd_change/')

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def plot(request):
    return render(request, 'plot.html')

def ajax_plotdata(request):
    to_return = {'stat': 'failed', 'data': ''}
    # fetch data by top interface, now generate random data
    length = 80
    d = [randint(0, 80) for i in range(length)]
    data = [[i, sum(d[:i+1])] for i in range(length)]
    to_return['stat'] = 'success'
    to_return['data'] = data
    
    serialized = simplejson.dumps(to_return)
    return HttpResponse(serialized, mimetype="application/json")

def pie(request):
    return render(request, 'pie.html')

def ajax_piedata(request):
    to_return = {'stat': 'failed', 'data': ''}
    to_return['data'] = [{'label': u'武汉', 'data': 10}, {'label': u'北京', 'data': 300}, {'label': u'上海', 'data': 420}, {'label': u'广州', 'data': 403}]
    serialized = simplejson.dumps(to_return)
    return HttpResponse(serialized, mimetype="application/json")


    