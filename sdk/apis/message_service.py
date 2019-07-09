# -*- coding: utf-8 -*-


# 消息服务
class MessageService:

    __client = None

    def __init__(self, client):
        self.__client = client

    def get_non_reached_messages(self, app_id):
        """
        获取未到达的推送消息
        :param appId:应用ID
        """
        return self.__client.call("eleme.message.getNonReachedMessages", {"appId": app_id})

    def get_non_reached_o_messages(self, app_id):
        """
        获取未到达的推送消息实体
        :param appId:应用ID
        """
        return self.__client.call("eleme.message.getNonReachedOMessages", {"appId": app_id})

    def query_failed_message_log(self, request):
        """
        获取http推送失败的消息
        :param request:查询推送失败消息日志结构体
        """
        return self.__client.call("eleme.message.queryFailedMessageLog", {"request": request})

