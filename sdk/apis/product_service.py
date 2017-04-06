# -*- coding: utf-8 -*-


# 商品服务
class ProductService:

    __client = None

    def __init__(self, client):
        self.__client = client

    # 获取一个分类下的所有商品
    def get_items_by_category_id(self, category_id):
        return self.__client.call("eleme.product.item.getItemsByCategoryId", {"categoryId": category_id})

    # 查询商品详情
    def get_item(self, item_id):
        return self.__client.call("eleme.product.item.getItem", {"itemId": item_id})

    # 批量查询商品详情
    def batch_get_items(self, item_ids):
        return self.__client.call("eleme.product.item.batchGetItems", {"itemIds": item_ids})

    # 添加商品
    def create_item(self, category_id, properties):
        return self.__client.call("eleme.product.item.createItem", {"categoryId": category_id, "properties": properties})

    # 批量添加商品
    def batch_create_items(self, category_id, items):
        return self.__client.call("eleme.product.item.batchCreateItems", {"categoryId": category_id, "items": items})

    # 更新商品
    def update_item(self, item_id, category_id, properties):
        return self.__client.call("eleme.product.item.updateItem", {"itemId": item_id, "categoryId": category_id, "properties": properties})

    # 批量置满库存
    def batch_fill_stock(self, spec_ids):
        return self.__client.call("eleme.product.item.batchFillStock", {"specIds": spec_ids})

    # 批量沽清库存
    def batch_clear_stock(self, spec_ids):
        return self.__client.call("eleme.product.item.batchClearStock", {"specIds": spec_ids})

    # 批量上架商品
    def batch_on_shelf(self, spec_ids):
        return self.__client.call("eleme.product.item.batchOnShelf", {"specIds": spec_ids})

    # 批量下架商品
    def batch_off_shelf(self, spec_ids):
        return self.__client.call("eleme.product.item.batchOffShelf", {"specIds": spec_ids})

    # 删除商品
    def remove_item(self, item_id):
        return self.__client.call("eleme.product.item.removeItem", {"itemId": item_id})

    # 批量删除商品
    def batch_remove_items(self, item_ids):
        return self.__client.call("eleme.product.item.batchRemoveItems", {"itemIds": item_ids})

    # 批量更新商品库存
    def batch_update_spec_stocks(self, spec_stocks):
        return self.__client.call("eleme.product.item.batchUpdateSpecStocks", {"specStocks": spec_stocks})

    # 设置商品排序
    def set_item_positions(self, category_id, item_ids):
        return self.__client.call("eleme.product.item.setItemPositions", {"categoryId": category_id, "itemIds": item_ids})

    # 查询店铺商品分类
    def get_shop_categories(self, shop_id):
        return self.__client.call("eleme.product.category.getShopCategories", {"shopId": shop_id})

    # 查询商品分类详情
    def get_category(self, category_id):
        return self.__client.call("eleme.product.category.getCategory", {"categoryId": category_id})

    # 添加商品分类
    def create_category(self, shop_id, name, description):
        return self.__client.call("eleme.product.category.createCategory", {"shopId": shop_id, "name": name, "description": description})

    # 更新商品分类
    def update_category(self, category_id, name, description):
        return self.__client.call("eleme.product.category.updateCategory", {"categoryId": category_id, "name": name, "description": description})

    # 删除商品分类
    def remove_category(self, category_id):
        return self.__client.call("eleme.product.category.removeCategory", {"categoryId": category_id})

    # 设置分类排序
    def set_category_positions(self, shop_id, category_ids):
        return self.__client.call("eleme.product.category.setCategoryPositions", {"shopId": shop_id, "categoryIds": category_ids})

    # 上传图片，返回图片的hash值
    def upload_image(self, image):
        return self.__client.call("eleme.file.uploadImage", {"image": image})

    # 通过远程URL上传图片，返回图片的hash值
    def upload_image_with_remote_url(self, url):
        return self.__client.call("eleme.file.uploadImageWithRemoteUrl", {"url": url})

    # 获取上传文件的访问URL，返回文件的Url地址
    def get_uploaded_url(self, hash):
        return self.__client.call("eleme.file.getUploadedUrl", {"hash": hash})

