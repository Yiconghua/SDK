# -*- coding: utf-8 -*-


# 活动服务
class ActivityService:

    __client = None

    def __init__(self, client):
        self.__client = client

    def get_invited_activity_infos(self, shop_id):
        """
        查询店铺邀约活动信息
        :param shopId:店铺Id
        """
        return self.__client.call("eleme.activity.flash.getInvitedActivityInfos", {"shopId": shop_id})

    def apply_flash_activity(self, activity_id, activity_apply_info):
        """
        报名限量抢购活动
        :param activityId:活动Id
        :param activityApplyInfo:活动报名信息
        """
        return self.__client.call("eleme.activity.flash.applyFlashActivity", {"activityId": activity_id, "activityApplyInfo": activity_apply_info})

    def get_activity_apply_infos(self, activity_id, shop_id, page_no, page_size):
        """
        通过店铺Id和活动Id分页查询报名详情
        :param activityId:活动Id
        :param shopId:店铺Id
        :param pageNo:页码
        :param pageSize:每页数量
        """
        return self.__client.call("eleme.activity.flash.getActivityApplyInfos", {"activityId": activity_id, "shopId": shop_id, "pageNo": page_no, "pageSize": page_size})

    def update_activity_item_stock(self, activity_id, shop_id, item_id, stock):
        """
        修改活动菜品库存
        :param activityId:活动Id
        :param shopId:店铺Id
        :param itemId:菜品Id
        :param stock:库存
        """
        return self.__client.call("eleme.activity.flash.updateActivityItemStock", {"activityId": activity_id, "shopId": shop_id, "itemId": item_id, "stock": stock})

    def offline_flash_activity_item(self, activity_id, shop_id, item_id):
        """
        取消活动菜品
        :param activityId:活动Id
        :param shopId:店铺Id
        :param itemId:菜品Id
        """
        return self.__client.call("eleme.activity.flash.offlineFlashActivityItem", {"activityId": activity_id, "shopId": shop_id, "itemId": item_id})

    def invalid_shop_activity(self, activity_id, shop_id):
        """
        作废店铺与活动的关联关系
        :param activityId:活动Id
        :param shopId:店铺Id
        """
        return self.__client.call("eleme.activity.flash.invalidShopActivity", {"activityId": activity_id, "shopId": shop_id})

