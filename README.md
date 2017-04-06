# Python SDK 接入指南 & CHANGELOG

## 接入指南
  1.安装eleme sdk依赖包,引入依赖
  2.利用sdk.config 模块初始化设置沙箱环境，key,secret 如果是企业应用还需设置callback_url
    利用sdk.oauth 模块完成oauth授权测试
    利用sdk.api 模块完成接口调用测试
    启动sdk自带的server 帮助完成接收饿了么推送消息业务处理
  3.上线前将config.py中初始值__sandbox,key和secret以及callback_url填为正式环境
 

## 代码示例

### 企业应用

  - 第一步 安装sdk 包,引入模块
  sudo pip install eleme.python.sdk

```python
    from sdk.library.oauth.oauth_client import OAuthClient
    from sdk.library.apis.shop_service import ShopService
    from sdk.library.protocol.rpc_client import RpcClient
    from sdk.config import Config
```
 
  - 第二步 实例化一个oauth2.0客户端授权模式的授权对象

```python
    oauth_client = OAuthClient(Config.get_app_key(), Config.get_secret(), Config.get_callback_url())
```

  - 第三步 获取生成授权url

```python
    auth_url = oauth_client.get_auth_url(state, scope)
```

  - 第四步 在授权url中同意授权后，会跳转到CALLBACK_URL的页面，在通过链接上的参数，获取授权码code


  - 第五️步 通过code获取token对象,此步获取到的token对象可在有效期内一直使用，不用每次调用前都去获取一次，建议应用授权一次后存放到全局缓存中

```python
    token = oauth_client.get_token_by_code(code)
```

  - 第六步 实例化远程调用的client对象

```python
	rpc_client = RpcClient(token, Config.get_app_key(), Config.get_secret(), Config.get_api_server_url())
```

  - 第七步 实例化一个服务对象

```python
    shop_service = ShopService(rpc_client)
```

  - 第八步 调用服务方法，获取资源数据

```python
    shop = shop_service.get_shop(123456)
```

  - 第九步 如果token过期，通过refresh_token换取新的token
```python
    refresh_token = token["refresh_token"]
    token = oauth_client.get_token_by_refresh_token(refresh_token, scope)
```

### 个人应用


  - 第一步 安装sdk 包,引入模块
    sodu install eleme.openapi.sdk

```python
    from sdk.oauth.oauth_client import OAuthClient
    from sdk.apis.shop_service import ShopService
    from sdk.protocol.rpc_client import RpcClient
    from sdk.config import Config
```

  - 第二步 实例化一个oauth2.0客户端授权模式的授权对象

```python
    oauth_client = OAuthClient(Config.get_app_key(), Config.get_secret(), Config.get_callback_url())
```

  - 第三️步 获取token对象,此步获取到的token对象可在有效期内一直使用，不用每次调用前都去获取一次，建议应用授权一次后存放到全局缓存中

```python
    token = oauth_client.get_token_in_client_credentials()
```

  - 第四步 实例化远程调用的client对象

```python
	rpc_client = RpcClient(token, Config.get_app_key(), Config.get_secret(), Config.get_api_server_url())
```

  - 第五步 实例化一个服务对象

```python
    shop_service = ShopService(rpc_client)
```

  - 第六步 调用服务方法，获取资源数据

```python
    shop = shop_service.get_shop(123456)
```
### simpleServer 使用方式
 - 第一步 安装sdk 包,引入模块
    sodu install eleme.openapi.sdk

```python
    from simpleserver.server import start_server
    from sdk.config import Config
```

  - 第二步 初始化config对象，启动服务

```python

    start_server()
```
    启动服务后 会监听三个localtion
    1.get  /listenMessage  响应饿了么平台的url校检
    2.post /listenMessage  接收饿了么平台的消息推送
    3.get  /callback       授权回调地址，处理授权逻辑
    4.post /getUserInfo    获取当前的用户信息和店铺信息




## CHANGELOG:

### [v1.1.2]

    Release Date : 2017-02-09

  - [BugFix] 修复了token获取的问题

### [v1.1.1]

    Release Date : 2017-01-24

  - [Feature] 重新支持个人应用授权，在oauth_client中添加get_token_in_client_credentials方法

### [v1.1.0]

    Release Date : 2017-01-24

  - [Feature] 更新了授权模式为企业应用授权，个人应用授权的方法不在支持，对应的工具类由client_credentials更换为oauth_client

### [v1.0.4]

    Release Date : 2017-01-19

- [Feature] 新增UserService

### [v1.0.3]

    Release Date : 2017-01-04

- [Improvement] token传入的时候由字符串改为对象，并添加了本地校验

### [v1.0.2]

    Release Date : 2016-12-21

- [Improvement] updateItem添加了参数categoryId


### [v1.0.1]

    Release Date : 2016-12-02

- [Improvement] 升级使用python3

  
### [v1.0.0]

    Release Date : 2016-11-19

- [Feature] sdk完整实现
- [Feature] 增加接口调用代码示例 demo/main.py
