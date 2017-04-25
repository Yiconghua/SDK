# -*- coding: utf-8 -*-

from sdk.config import Config
from sdk.oauth.oauth_client import OAuthClient
from sdk.protocol.rpc_client import RpcClient
from sdk.apis.user_service import UserService
from sdk.apis.order_service import OrderService
from sdk.apis.product_service import ProductService

import json

class MyLog:
    def info(self, log):
        print (u"my info log:{}".format(log))

    def error(self, log):
        print (u"my error log:{}".format(log))



config = Config(True, 'avGYo8TAFL', 'fc6e4922bda4148ab4a734f5acbe58a7ce3a684a', callback_url=None)
config.set_log(MyLog())
config.set_base_url("https://open-api-sandbox-shop.alpha.elenet.me")
config.get_log().info("wwwwwwww")
#config = Config(True, 'ja7rOj8Zkj', '4573a5f70a349661a8ce6489696e07d0e7d5a9b9', None, "https://open-api-sandbox-shop.alpha.elenet.me")


def get_token():
    oauth_client = OAuthClient(config)
    result = oauth_client.get_token_in_client_credentials()
    print(result)
    return result


def get_token_by_auth_code():
    oauth_client = OAuthClient(config)
    auth_url = oauth_client.get_token_by_auth_code('864e688f17b624f866ab509009ef782e')
    print (auth_url)


def user_get_user(token):
    client = RpcClient(config, token)
    user_service = UserService(client)
    response = user_service.get_user()
    print (response)

def batch_on_shelf(token):
    client = RpcClient(config, token)
    response = ProductService(client).create_item(category_id=26940000135,
                                                  properties={
                                                      'name': "白切鸡",
                                                      'description': "香脆可口，外焦里嫩",
                                                      'imageHash': "3077080f760e7bf0fc985e23dd3e36e2",
                                                      'labels': {
                                                          'isFeatured': 1,
                                                          'isGum': 0,
                                                          'isNew': 0,
                                                          'isSpicy': 0
                                                      },
                                                      'specs': [
                                                          {
                                                              'specId': 72970000222,
                                                              'name': "大份",
                                                              'price': 18.0,
                                                              'stock': 9000,
                                                              'maxStock': 10000,
                                                              'packingFee': 3.0,
                                                              'onShelf': 1,
                                                              'extendCode': "1234567890",
                                                              'barCode': "X148948686356666",
                                                              'weight': 123
                                                          }
                                                      ],
                                                      'sellingTime': {
                                                          'weeks': [
                                                              'MONDAY',
                                                              'TUESDAY',
                                                              'WEDNESDAY',
                                                              'THURSDAY',
                                                              'FRIDAY',
                                                              'SATURDAY',
                                                              'SUNDAY'
                                                          ],
                                                          'beginDate': "2017-03-14",
                                                          'endDate': "2017-06-22",
                                                          'times': [
                                                              {
                                                                  'beginTime': "18:02",
                                                                  'endTime': "19:02"
                                                              }
                                                          ]
                                                      },
                                                      'attributes': [
                                                          {
                                                              'name': "甜度",
                                                              'details': [
                                                                  "5分甜",
                                                                  "7分甜"
                                                              ]
                                                          }
                                                      ]
                                                  })
    print (response)


def product_create_item():
    pass



if __name__ == '__main__':
    #sdklog= MyLog()
    token = json.loads(get_token())['access_token']
    print (token)
    #########test user_service#########
    batch_on_shelf(token)
    #order_get_order(token,'12312341234')
    #get_token_by_auth_code()


