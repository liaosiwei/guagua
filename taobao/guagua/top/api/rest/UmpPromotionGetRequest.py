'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class UmpPromotionGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.channel_key = None
		self.item_id = None

	def getapiname(self):
		return 'taobao.ump.promotion.get'
