# -*- coding: utf-8 -*-


# 商品服务
class ProductService:

    __client = None

    def __init__(self, client):
        self.__client = client

    def get_items_by_category_id(self, category_id):
        """
        获取一个分类下的所有商品
        :param categoryId:商品分类Id
        """
        return self.__client.call("eleme.product.item.getItemsByCategoryId", {"categoryId": category_id})

    def get_item(self, item_id):
        """
        查询商品详情
        :param itemId:商品Id
        """
        return self.__client.call("eleme.product.item.getItem", {"itemId": item_id})

    def batch_get_items(self, item_ids):
        """
        批量查询商品详情
        :param itemIds:商品Id的列表
        """
        return self.__client.call("eleme.product.item.batchGetItems", {"itemIds": item_ids})

    def create_item(self, category_id, properties):
        """
        添加商品
        :param categoryId:商品分类Id
        :param properties:商品属性
        """
        return self.__client.call("eleme.product.item.createItem", {"categoryId": category_id, "properties": properties})

    def batch_create_items(self, category_id, items):
        """
        批量添加商品
        :param categoryId:商品分类Id
        :param items:商品属性的列表
        """
        return self.__client.call("eleme.product.item.batchCreateItems", {"categoryId": category_id, "items": items})

    def update_item(self, item_id, category_id, properties):
        """
        更新商品
        :param itemId:商品Id
        :param categoryId:商品分类Id
        :param properties:商品属性
        """
        return self.__client.call("eleme.product.item.updateItem", {"itemId": item_id, "categoryId": category_id, "properties": properties})

    def batch_fill_stock(self, spec_ids):
        """
        批量置满库存
        :param specIds:商品及商品规格的列表
        """
        return self.__client.call("eleme.product.item.batchFillStock", {"specIds": spec_ids})

    def batch_clear_stock(self, spec_ids):
        """
        批量沽清库存
        :param specIds:商品及商品规格的列表
        """
        return self.__client.call("eleme.product.item.batchClearStock", {"specIds": spec_ids})

    def batch_on_shelf(self, spec_ids):
        """
        批量上架商品
        :param specIds:商品及商品规格的列表
        """
        return self.__client.call("eleme.product.item.batchOnShelf", {"specIds": spec_ids})

    def batch_off_shelf(self, spec_ids):
        """
        批量下架商品
        :param specIds:商品及商品规格的列表
        """
        return self.__client.call("eleme.product.item.batchOffShelf", {"specIds": spec_ids})

    def remove_item(self, item_id):
        """
        删除商品
        :param itemId:商品Id
        """
        return self.__client.call("eleme.product.item.removeItem", {"itemId": item_id})

    def batch_remove_items(self, item_ids):
        """
        批量删除商品
        :param itemIds:商品Id的列表
        """
        return self.__client.call("eleme.product.item.batchRemoveItems", {"itemIds": item_ids})

    def batch_update_spec_stocks(self, spec_stocks):
        """
        批量更新商品库存
        :param specStocks:商品以及规格库存列表
        """
        return self.__client.call("eleme.product.item.batchUpdateSpecStocks", {"specStocks": spec_stocks})

    def set_item_positions(self, category_id, item_ids):
        """
        设置商品排序
        :param categoryId:商品分类Id
        :param itemIds:商品Id列表
        """
        return self.__client.call("eleme.product.item.setItemPositions", {"categoryId": category_id, "itemIds": item_ids})

    def get_shop_categories(self, shop_id):
        """
        查询店铺商品分类
        :param shopId:店铺Id
        """
        return self.__client.call("eleme.product.category.getShopCategories", {"shopId": shop_id})

    def get_category(self, category_id):
        """
        查询商品分类详情
        :param categoryId:商品分类Id
        """
        return self.__client.call("eleme.product.category.getCategory", {"categoryId": category_id})

    def create_category(self, shop_id, name, description):
        """
        添加商品分类
        :param shopId:店铺Id
        :param name:商品分类名称，长度需在50字以内
        :param description:商品分类描述，长度需在50字以内
        """
        return self.__client.call("eleme.product.category.createCategory", {"shopId": shop_id, "name": name, "description": description})

    def update_category(self, category_id, name, description):
        """
        更新商品分类
        :param categoryId:商品分类Id
        :param name:商品分类名称，长度需在50字以内
        :param description:商品分类描述，长度需在50字以内
        """
        return self.__client.call("eleme.product.category.updateCategory", {"categoryId": category_id, "name": name, "description": description})

    def remove_category(self, category_id):
        """
        删除商品分类
        :param categoryId:商品分类Id
        """
        return self.__client.call("eleme.product.category.removeCategory", {"categoryId": category_id})

    def set_category_positions(self, shop_id, category_ids):
        """
        设置分类排序
        :param shopId:饿了么店铺Id
        :param categoryIds:需要排序的分类Id
        """
        return self.__client.call("eleme.product.category.setCategoryPositions", {"shopId": shop_id, "categoryIds": category_ids})

    def upload_image(self, image):
        """
        上传图片，返回图片的hash值
        :param image:文件内容base64编码值
        """
        return self.__client.call("eleme.file.uploadImage", {"image": image})

    def upload_image_with_remote_url(self, url):
        """
        通过远程URL上传图片，返回图片的hash值
        :param url:远程Url地址
        """
        return self.__client.call("eleme.file.uploadImageWithRemoteUrl", {"url": url})

    def get_uploaded_url(self, hash):
        """
        获取上传文件的访问URL，返回文件的Url地址
        :param hash:图片hash值
        """
        return self.__client.call("eleme.file.getUploadedUrl", {"hash": hash})

