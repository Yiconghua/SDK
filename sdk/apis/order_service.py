# -*- coding: utf-8 -*-


# 订单服务
class OrderService:

    __client = None

    def __init__(self, client):
        self.__client = client

    def get_order(self, order_id):
        """
        获取订单
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.getOrder", {"orderId": order_id})

    def mget_orders(self, order_ids):
        """
        批量获取订单
        :param orderIds:订单Id的列表
        """
        return self.__client.call("eleme.order.mgetOrders", {"orderIds": order_ids})

    def confirm_order(self, order_id):
        """
        确认订单
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.confirmOrder", {"orderId": order_id})

    def cancel_order(self, order_id, type, remark):
        """
        取消订单
        :param orderId:订单Id
        :param type:取消原因
        :param remark:备注说明
        """
        return self.__client.call("eleme.order.cancelOrder", {"orderId": order_id, "type": type, "remark": remark})

    def agree_refund(self, order_id):
        """
        同意退单/取消单
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.agreeRefund", {"orderId": order_id})

    def disagree_refund(self, order_id, reason):
        """
        不同意退单/取消单
        :param orderId:订单Id
        :param reason:商家不同意退单原因
        """
        return self.__client.call("eleme.order.disagreeRefund", {"orderId": order_id, "reason": reason})

    def get_delivery_state_record(self, order_id):
        """
        获取订单配送记录
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.getDeliveryStateRecord", {"orderId": order_id})

    def batch_get_delivery_states(self, order_ids):
        """
        批量获取订单最新配送记录
        :param orderIds:订单Id列表
        """
        return self.__client.call("eleme.order.batchGetDeliveryStates", {"orderIds": order_ids})

    def delivery_by_self(self, order_id):
        """
        配送异常或者物流拒单后选择自行配送
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.deliveryBySelf", {"orderId": order_id})

    def no_more_delivery(self, order_id):
        """
        配送异常或者物流拒单后选择不再配送
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.noMoreDelivery", {"orderId": order_id})

