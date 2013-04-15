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