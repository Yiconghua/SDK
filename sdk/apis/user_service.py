# -*- coding: utf-8 -*-


# 商户服务
class UserService:

    __client = None

    def __init__(self, client):
        self.__client = client

    def get_user(self):
        """
        获取商户账号信息
        """
        return self.__client.call("eleme.user.getUser", {})

