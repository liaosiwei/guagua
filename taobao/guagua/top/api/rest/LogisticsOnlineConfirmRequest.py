'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class LogisticsOnlineConfirmRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.out_sid = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.online.confirm'
