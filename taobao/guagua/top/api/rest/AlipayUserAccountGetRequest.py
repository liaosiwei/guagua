'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class AlipayUserAccountGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'alipay.user.account.get'
