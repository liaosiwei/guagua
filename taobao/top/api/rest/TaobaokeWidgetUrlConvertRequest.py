'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class TaobaokeWidgetUrlConvertRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.outer_code = None
		self.url = None

	def getapiname(self):
		return 'taobao.taobaoke.widget.url.convert'
