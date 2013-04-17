# coding=UTF-8
import base64
from random import randint
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect

import top as taobao
import top.api as topapi
# next for online app
#taobao.setDefaultAppInfo("21446815", "5e8279097b48bd0eefcec5f48c7381eb")
# next for sandbox test
taobao.setDefaultAppInfo("1021446815", "sandbox97b48bd0eefcec5f48c7381eb")
sessionkey = None
print 'hello there'
def top(api_name, **kwarg):
    global sessionkey
    
    if hasattr(topapi, api_name):
        api = getattr(topapi, api_name)
    else:
        raise ImportError('no api found')
    # 测试用
    authrize = None
    a = api("gw.api.tbsandbox.com")
    #sdbsessionkey = '6101f23c7a9a2e8d90b4c74fbfd2bc21283630269ab37d42066555142' #user: sandbox_seller_0
    #sdbsessionkey = '6100c248a74c1e577ca89bd9b89f574a18a8f16a31452282076226627' # user: sandbox_b_20
    # 上线环境用 
    # a = api()
    while kwarg:
        key, value = kwarg.popitem()
        if hasattr(a, key):
            setattr(a, key, value)
        else:
            if key is 'authrized' and value is 1:
                authrize = sessionkey
            elif key is not 'authrized':
                raise AttributeError('some attributes do not exist!')    
    return a.getResponse(authrize)
    
def fetchsession(request):
    global sessionkey
    
    if request.method == 'GET':
        get = request.GET.copy()
        if get.has_key('top_session'):
            sessionkey = get['top_session']
        if get.has_key('top_parameters'):
            para_str = base64.b64decode(get['top_parameters'])
            para_dict = dict([tuple(itme.split('=')) for item in para_str.split('&')])
            
    return HttpResponseRedirect('/')

def base(request):
    return render_to_response('base.html')

def index(request):
    return render_to_response('index.html')

def plot(request):
    return render_to_response('plot.html')

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
    return render_to_response('pie.html')

def ajax_piedata(request):
    to_return = {'stat': 'failed', 'data': ''}
    to_return['data'] = [{'label': u'武汉', 'data': 10}, {'label': u'北京', 'data': 300}, {'label': u'上海', 'data': 420}, {'label': u'广州', 'data': 403}]
    serialized = simplejson.dumps(to_return)
    return HttpResponse(serialized, mimetype="application/json")


    