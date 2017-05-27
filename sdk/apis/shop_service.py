# -*- coding: utf-8 -*-


# 店铺服务
class ShopService:

    __client = None

    def __init__(self, client):
        self.__client = client

    def get_shop(self, shop_id):
        """
        查询店铺信息
        :param shopId:店铺Id
        """
        return self.__client.call("eleme.shop.getShop", {"shopId": shop_id})

    def update_shop(self, shop_id, properties):
        """
        更新店铺基本信息
        :param shopId:店铺Id
        :param properties:店铺属性
        """
        return self.__client.call("eleme.shop.updateShop", {"shopId": shop_id, "properties": properties})

    def mget_shop_status(self, shop_ids):
        """
        批量获取店铺简要
        :param shopIds:店铺Id的列表
        """
        return self.__client.call("eleme.shop.mgetShopStatus", {"shopIds": shop_ids})

    def set_delivery_time(self, shop_id, delivery_basic_mins, delivery_adjust_mins):
        """
        设置送达时间
        :param shopId:店铺Id
        :param deliveryBasicMins:配送基准时间(单位分钟)
        :param deliveryAdjustMins:配送调整时间(单位分钟)
        """
        return self.__client.call("eleme.shop.setDeliveryTime", {"shopId": shop_id, "deliveryBasicMins": delivery_basic_mins, "deliveryAdjustMins": delivery_adjust_mins})

    def set_online_refund(self, shop_id, enable):
        """
        设置是否支持在线退单
        :param shopId:店铺Id
        :param enable:是否支持
        """
        return self.__client.call("eleme.shop.setOnlineRefund", {"shopId": shop_id, "enable": enable})

