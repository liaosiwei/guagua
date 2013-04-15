'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class CaipiaoPresentStatGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.days = None

	def getapiname(self):
		return 'taobao.caipiao.present.stat.get'
