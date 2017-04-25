from sdk.config import Config
from server.global_config import Global
from server.start_up import boot_start
if __name__ == '__main__':
    #"https://open-api-sandbox-shop.alpha.elenet.me"
    config = Config(True, 'avGYo8TAFL', 'fc6e4922bda4148ab4a734f5acbe58a7ce3a684a', None)
    config.set_log()
    config.set_base_url("https://open-api-sandbox-shop.alpha.elenet.me")
    Global(config)
    # Config(True, 'ja7rOj8Zkj', '4573a5f70a349661a8ce6489696e07d0e7d5a9b9',
    #           'http://vpca-phoenix-buttonwood-service-1.vm.elenet.me:8080/callback', "https://open-api-sandbox-shop.alpha.elenet.me")
    boot_start(8111)