# -*- coding: utf-8 -*-


# 订单评论服务
class UgcService:

    __client = None

    def __init__(self, client):
        self.__client = client

    def query_order_comments(self, shop_id, offset, limit):
        """
        openAPI 查询近2周的评论
        :param shopId:店铺Id
        :param offset:分页偏移
        :param limit:单页数据
        """
        return self.__client.call("eleme.ugc.queryOrderComments", {"shopId": shop_id, "offset": offset, "limit": limit})

    def count_order_comments(self, shop_id):
        """
        openAPI 查询近2周的评论数量
        :param shopId:店铺Id
        """
        return self.__client.call("eleme.ugc.countOrderComments", {"shopId": shop_id})

    def reply_order_comment(self, shop_id, comment_id, content, replier_name):
        """
        openAPI 回复评论接口
        :param shopId:店铺Id
        :param commentId:评论id
        :param content:回复内容
        :param replierName:回复人
        """
        return self.__client.call("eleme.ugc.replyOrderComment", {"shopId": shop_id, "commentId": comment_id, "content": content, "replierName": replier_name})

