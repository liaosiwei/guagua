'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class UdpItemGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.area = None
		self.begin_time = None
		self.end_time = None
		self.fields = None
		self.itemid = None
		self.items = None
		self.order_by = None
		self.order_rule = None
		self.page_no = None
		self.page_size = None
		self.parameters = None
		self.source = None

	def getapiname(self):
		return 'taobao.udp.item.get'
