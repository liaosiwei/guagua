'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class UmpDetailListAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.act_id = None
		self.details = None

	def getapiname(self):
		return 'taobao.ump.detail.list.add'
