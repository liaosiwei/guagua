'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class SimbaInsightWordsbaseGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.filter = None
		self.nick = None
		self.time = None
		self.words = None

	def getapiname(self):
		return 'taobao.simba.insight.wordsbase.get'
