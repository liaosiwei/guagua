'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class TopatsItemsAllGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.fields = None
		self.start_time = None
		self.status = None

	def getapiname(self):
		return 'taobao.topats.items.all.get'
