'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class FenxiaoProductImageDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.position = None
		self.product_id = None
		self.properties = None

	def getapiname(self):
		return 'taobao.fenxiao.product.image.delete'
