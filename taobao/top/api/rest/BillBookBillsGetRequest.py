'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class BillBookBillsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.account_id = None
		self.end_time = None
		self.fields = None
		self.journal_types = None
		self.page_no = None
		self.page_size = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.bill.book.bills.get'
