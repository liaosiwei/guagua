'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class AlibabaLogisticsOrderCancelRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.order_id = None
		self.reason = None

	def getapiname(self):
		return 'alibaba.logistics.order.cancel'
