# Python SDK 接入指南 & CHANGELOG

## 接入指南
    1. 安装eleme sdk依赖包,引入依赖
    2. 利用sdk.config 模块初始化设置沙箱环境，key,secret,调用config.set_log 设置自己的log处理方式。如果是企业应用还需设置callback_url
    3. 利用sdk.oauth 模块完成oauth授权测试
    4. 利用sdk.api 模块完成接口调用测试
    5. 启动sdk自带的server 帮助完成接收饿了么推送消息业务,以及授权测试
    6. 上线前将config.py中初始值sandbox,key和secret以及callback_url填为正式环境


## 代码示例(以调用ShopService为例)


### 企业应用

  - 第一步 安装sdk 包,引入模块
  sudo pip install eleme.openapi.python.sdk

```python
    from sdk.oauth.oauth_client import OAuthClient
    from sdk.apis.shop_service import ShopService
    from sdk.config import Config
```
 
  - 第二步  实例化一个config,设置自己的日志处理方式 实例化一个oauth2.0客户端授权模式的授权对象

```python
    config = Config(True, key, secret, call_back_url)
    # 自己的日志处理方式,必须有info 和error 方法
    class MyLog:
        def info(self, log):
            print (u"my info log:{}".format(log))

        def error(self, log):
            print (u"my error log:{}".format(log))

    config.set_log(MyLog())
    oauth_client = OAuthClient(config)
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
    rpc_client = RpcClient(config, token)
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
    sudo pip install eleme.openapi.python.sdk

```python
    from sdk.oauth.oauth_client import OAuthClient
    from sdk.apis.shop_service import ShopService
    from sdk.protocol.rpc_client import RpcClient
    from sdk.config import Config
```

  - 第二步 实例化config对象，实例化一个oauth2.0客户端授权模式的授权对象

```python
    config = Config(True, key, secret)
    # 自己的日志处理方式,必须有info 和error 方法
    class MyLog:
        def info(self, log):
            print (u"my info log:{}".format(log))

        def error(self, log):
            print (u"my error log:{}".format(log))

    config.set_log(MyLog())
    oauth_client = OAuthClient(config)
```

  - 第三️步 获取token对象,此步获取到的token对象可在有效期内一直使用，不用每次调用前都去获取一次，建议应用授权一次后存放到全局缓存中

```python
    token = oauth_client.get_token_in_client_credentials()
```

  - 第四步 实例化远程调用的client对象

```python
    rpc_client = RpcClient(config, token)
```

  - 第五步 实例化一个服务对象

```python
    shop_service = ShopService(rpc_client)
```

  - 第六步 调用服务方法，获取资源数据

```python
    shop = shop_service.get_shop(123456)
```


### Server 使用方式

 - 第一步 安装sdk 包,引入模块
    sudo pip install eleme.openapi.python.sdk

 - 第二步 引入依赖

```python
    from sdk.config import Config
    from server.global_config import Global
    from server.start_up import boot_start
```
 - 第三步 初始化config对象,并将config对象设置到Global中

```python
    config = Config(True, key, secret, call_back_url)
    # 自己的日志处理方式,必须有info 和error 方法
    class MyLog:
        def info(self, log):
            print (u"my info log:{}".format(log))

        def error(self, log):
            print (u"my error log:{}".format(log))

    config.set_log(MyLog())
    Global(config)
```

 - 第四步 启动服务
 启动服务后 会监听三个localtion
    1. get  /listenMessage  响应饿了么平台的url校检
    2. post /listenMessage  接收饿了么平台的消息推送
    3. get  /callback       授权回调地址，处理授权逻辑
    4. post /getInfo        获取当前的用户信息和店铺信息

```python
    boot_start(port)
```




## CHANGELOG:

### [v1.0.0]

    Release Date : 2017-04-07

  - [feature] eleme sdk

### [v1.0.1]

    Release Date : 2017-04-11

  - [feature] 1.文档优化;2.修改回调页面图标

### [v1.1.0]

    Release Date : 2017-04-25

  - [feature] 1.增加ugc服务;2.订单服务增加确认送达接口;3.shop服务增加设置送达时间接口;4.product服务增加 批量沽清置满接口

### [v1.1.1]

    Release Date : 2017-04-28

  - [bugfix] 1.为和老版本使用习惯保持一致,RpcClient(config,token) 中的token含义由access_token改为含有access_token 属性的json串
	
### [v1.2.0]

    Release Date : 2017-05-05

  - [feature]
  1.增加签约服务;
  2.订单服务中新增了 eleme.order.replyReminder eleme.order.getCommodities eleme.order.mgetCommodities eleme.order.getRefundOrder eleme.order.mgetRefundOrders
  3.增加接口查询商品后台分类 eleme.product.category.getBackCategory


