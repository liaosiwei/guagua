'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class IncrementTradesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_modified = None
		self.nick = None
		self.page_no = None
		self.page_size = None
		self.start_modified = None
		self.status = None
		self.type = None

	def getapiname(self):
		return 'taobao.increment.trades.get'
