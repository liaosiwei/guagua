'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class TopatsTradesSoldGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.fields = None
		self.is_acookie = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.topats.trades.sold.get'
