# -*- coding: utf-8 -*-


# 企业订餐商户服务
class EnterpriseService:

    __client = None

    def __init__(self, client):
        self.__client = client

    def update_ent_arrival_order_relate(self, relate_req_dto):
        """
        关联企业订餐到店订单
        :param relateReqDto:订单关联请求
        """
        return self.__client.call("eleme.enterprise.updateEntArrivalOrderRelate", {"relateReqDto": relate_req_dto})

    def update_ent_arrival_shop_enable(self, enable_request):
        """
        更新企业订餐店铺订单关联启用状态
        :param enableRequest:门店启用请求
        """
        return self.__client.call("eleme.enterprise.updateEntArrivalShopEnable", {"enableRequest": enable_request})

