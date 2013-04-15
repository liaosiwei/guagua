'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class BillBillGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.bid = None
		self.fields = None

	def getapiname(self):
		return 'taobao.bill.bill.get'
