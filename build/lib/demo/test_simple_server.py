from server.server import start_server
from sdk.config import Config
if __name__ == "__main__":
    Config(True, 'avGYo8TAFL', 'fc6e4922bda4148ab4a734f5acbe58a7ce3a684a', 'http://vpca-phoenix-buttonwood-service-1.vm.elenet.me:8080/callback',
           "https://open-api-sandbox-shop.alpha.elenet.me")
    start_server()
