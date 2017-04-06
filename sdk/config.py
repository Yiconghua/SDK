# -*- coding: utf-8 -*-
class Config:
    __sandbox = False
    # your app_key
    __app_key = None
    # your secret
    __secret = None

    __log_path = None
    # your callback url
    __callback_url = None

    __base_url = None

    def __init__(self, sandbox, app_key, secret, callback_url=None):
        Config.__sandbox = sandbox
        Config.__app_key = app_key
        Config.__secret = secret
        Config.__callback_url = callback_url

    @staticmethod
    def get_app_key():
        return Config.__app_key

    @staticmethod
    def set_base_url(base_url):
        Config.__base_url = base_url

    @staticmethod
    def set_log_path(log_path):
        Config.__log_path = log_path

    @staticmethod
    def get_secret():
        return Config.__secret

    @staticmethod
    def get_callback_url():
        return Config.__callback_url

    @staticmethod
    def get_log_path():
        return Config.__log_path

    @staticmethod
    def get_server_url():
        if not Config.__base_url:
            return Config.__sandbox and "https://open-api-sandbox.shop.ele.me" or "https://open-api.shop.ele.me"
        else:
            return Config.__base_url

    @staticmethod
    def get_access_token_url():
        return Config.get_server_url() + "/token"

    @staticmethod
    def get_api_server_url():
        return Config.get_server_url() + "/api/v1/"

    @staticmethod
    def get_authorize_url():
        return Config.get_server_url() + "/authorize"
