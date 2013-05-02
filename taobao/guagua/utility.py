# coding=UTF-8
import StringIO
import json
from urllib2 import urlopen
from zipfile import ZipFile
from time import sleep
from django.contrib.auth.models import User
from models import TradeSoldRecord
import top as taobao
import top.api as topapi
# next for online app
#taobao.setDefaultAppInfo("21446815", "5e8279097b48bd0eefcec5f48c7381eb")
# next for sandbox test
taobao.setDefaultAppInfo("1021446815", "sandbox97b48bd0eefcec5f48c7381eb")

# top(): 用于获取数据的函数接口
# 参数： 1. api_name: 需要调用的函数名称； 2. kwarg: 需要传入的参数; 3.sessionkey: 作为关键字参数传入sessionkey，如果没有该关键字则表示不使用sessionkey
# 返回值： 正常返回json格式的数据，发生错误时返回异常
# 例子： top('UserGetRequest', fields='nick, sex', [id=XX]) 
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
    id = kwarg.pop('id', 0)
    if id:
        authrize = User.objects.get(id=id).userprofile.sessionkey
    else:
        authrize = None
    while kwarg:
        key, value = kwarg.popitem()
        if hasattr(a, key):
            setattr(a, key, value)
        else:
            raise AttributeError('attribute %s do not exist!' % key)    
    return a.getResponse(authrize)

def test_asyn_done(task_id):
    flag = 1
    count = 0
    while flag:
        count += 1
        if count >= 360:
            break
        res = top('TopatsResultGet', task_id=task_id)
        if res['topats_result_get_response']['task']['status'] == 'done':
            flag = 0
        else:
            sleep(5)
    return ((flag and [0] or [1])[0], res)

# asyn function to get trade sold data between start_time and end_time. E.g
# top('TopatsTradesSoldGet', id=2, fields='tid, buyer_nick, payment', start_time='20130301', end_time='20130331') trying 3590110
def trade_sold_get(id, start_time, end_time):
    res = top('TopatsTradesSoldGet', id=id, fields='tid, buyer_nick, buyer_area, payment, created', start_time=start_time, end_time=end_time)
    task_id = res['topats_trades_sold_get_response']['task']['task_id']
    status, result = test_asyn_done(task_id)
    if status:
        print 'access data succeeded'
        url = result['topats_result_get_response']['task']['download_url']
        try:
            u = urlopen(url)
        except:
            return None
        s = StringIO.StringIO()
        s.write(u.read())
        z = ZipFile(s)
        filelist = z.namelist()
        user = User.objects.get(id=id)
        for filename in filelist:
            f = z.open(filename)
            for line in f: # line: {"trade_fullinfo_get_response":{"trade":{"buyer_nick":"sandbox_c_2","payment":"10.00","tid":92132032608727}}}
                d = json.JSONDecoder()
                r = d.decode(line)['trade_fullinfo_get_response']['trade']
                TradeSoldRecord.objects.create(user=user, buyer_nick=r['buyer_nick'], buyer_area=r['buyer_area'], 
                                               tid=r['tid'], payment=r['payment'], created=r['created'])
        return 1
    else:
        return 0
                
def trade_inc_get(id, start_time, end_time):
    res = top('TradesSoldIncrementGet', id=id, fields='tid, buyer_nick, buyer_area, payment, created', start_modified=start_time, end_modified=end_time)
    
    