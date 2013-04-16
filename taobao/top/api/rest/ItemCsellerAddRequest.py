'''
Created by auto_sdk on 2013-04-14 16:35:32
'''
from top.api.base import RestApi
class ItemCsellerAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.after_sale_id = None
		self.approve_status = None
		self.auto_fill = None
		self.auto_repost = None
		self.cid = None
		self.cod_postage_id = None
		self.desc = None
		self.ems_fee = None
		self.express_fee = None
		self.features = None
		self.freight_payer = None
		self.global_stock_type = None
		self.has_discount = None
		self.has_invoice = None
		self.has_showcase = None
		self.has_warranty = None
		self.increment = None
		self.inner_shop_auction_template_id = None
		self.input_pids = None
		self.input_str = None
		self.is_3D = None
		self.is_ex = None
		self.is_lightning_consignment = None
		self.is_taobao = None
		self.is_xinpin = None
		self.item_size = None
		self.item_spec_prop = None
		self.item_weight = None
		self.lang = None
		self.list_time = None
		self.locality_life_choose_logis = None
		self.locality_life_expirydate = None
		self.locality_life_merchant = None
		self.locality_life_network_id = None
		self.locality_life_onsale_auto_refund_ratio = None
		self.locality_life_refund_ratio = None
		self.locality_life_verification = None
		self.location_city = None
		self.location_state = None
		self.num = None
		self.outer_id = None
		self.outer_shop_auction_template_id = None
		self.pic_path = None
		self.post_fee = None
		self.postage_id = None
		self.price = None
		self.property_alias = None
		self.props = None
		self.second_kill = None
		self.sell_promise = None
		self.seller_cids = None
		self.sku_outer_ids = None
		self.sku_prices = None
		self.sku_properties = None
		self.sku_quantities = None
		self.sku_spec_ids = None
		self.stuff_status = None
		self.sub_pic_paths = None
		self.sub_stock = None
		self.title = None
		self.type = None
		self.valid_thru = None
		self.weight = None

	def getapiname(self):
		return 'taobao.item.cseller.add'

	def getTranslateParas(self):
		return {'location_state':'location.state','locality_life_onsale_auto_refund_ratio':'locality_life.onsale_auto_refund_ratio','locality_life_choose_logis':'locality_life.choose_logis','locality_life_network_id':'locality_life.network_id','locality_life_merchant':'locality_life.merchant','location_city':'location.city','locality_life_expirydate':'locality_life.expirydate','locality_life_verification':'locality_life.verification','locality_life_refund_ratio':'locality_life.refund_ratio'}
