# coding=UTF-8
from random import randint
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse



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
    to_return['data'] = [{'label': u'武汉', 'data': 200}, {'label': u'北京', 'data': 300}, {'label': u'上海', 'data': 420}, {'label': u'广州', 'data': 403}]
    serialized = simplejson.dumps(to_return)
    return HttpResponse(serialized, mimetype="application/json")
    