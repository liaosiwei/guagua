'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class WidgetItempanelGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.item_id = None

	def getapiname(self):
		return 'taobao.widget.itempanel.get'
