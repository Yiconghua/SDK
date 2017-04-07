# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from sdk.config import Config
from server.server_handle import application
import sys
if sys.version < '3':
    reload(sys)
    sys.setdefaultencoding('utf8')

config = None

def boot_start(port,config):
    config = config
    httpd = make_server('', port, application)
    print('Serving HTTP on port {}...'.format(port))
    httpd.serve_forever()

if __name__ == '__main__':
    #"https://open-api-sandbox-shop.alpha.elenet.me"
    config = Config(True, 'avGYo8TAFL', 'fc6e4922bda4148ab4a734f5acbe58a7ce3a684a', None)
    config.set_base_url("https://open-api-sandbox-shop.alpha.elenet.me")
    # Config(True, 'ja7rOj8Zkj', '4573a5f70a349661a8ce6489696e07d0e7d5a9b9',
    #           'http://vpca-phoenix-buttonwood-service-1.vm.elenet.me:8080/callback', "https://open-api-sandbox-shop.alpha.elenet.me")
    boot_start(8111, config)
