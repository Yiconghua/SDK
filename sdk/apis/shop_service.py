# -*- coding: utf-8 -*-


# 店铺服务
class ShopService:

    __client = None

    def __init__(self, client):
        self.__client = client

    # 查询店铺信息
    def get_shop(self, shop_id):
        return self.__client.call("eleme.shop.getShop", {"shopId": shop_id})

    # 更新店铺基本信息
    def update_shop(self, shop_id, properties):
        return self.__client.call("eleme.shop.updateShop", {"shopId": shop_id, "properties": properties})

    # 批量获取店铺简要
    def mget_shop_status(self, shop_ids):
        return self.__client.call("eleme.shop.mgetShopStatus", {"shopIds": shop_ids})

