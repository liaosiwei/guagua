# coding=UTF-8
import base64
from random import randint
from django.shortcuts import render
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from utility import *

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


    