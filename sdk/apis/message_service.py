# -*- coding: utf-8 -*-


# 消息服务
class MessageService:

    __client = None

    def __init__(self, client):
        self.__client = client

    # 获取未到达的推送消息
    def get_non_reached_messages(self, app_id):
        return self.__client.call("eleme.message.getNonReachedMessages", {"appId": app_id})

    # 获取未到达的推送消息实体
    def get_non_reached_o_messages(self, app_id):
        return self.__client.call("eleme.message.getNonReachedOMessages", {"appId": app_id})

