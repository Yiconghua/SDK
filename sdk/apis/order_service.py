# -*- coding: utf-8 -*-


# 订单服务
class OrderService:

    __client = None

    def __init__(self, client):
        self.__client = client

    # 获取订单
    def get_order(self, order_id):
        return self.__client.call("eleme.order.getOrder", {"orderId": order_id})

    # 批量获取订单
    def mget_orders(self, order_ids):
        return self.__client.call("eleme.order.mgetOrders", {"orderIds": order_ids})

    # 确认订单
    def confirm_order(self, order_id):
        return self.__client.call("eleme.order.confirmOrder", {"orderId": order_id})

    # 取消订单
    def cancel_order(self, order_id, type, remark):
        return self.__client.call("eleme.order.cancelOrder", {"orderId": order_id, "type": type, "remark": remark})

    # 同意退单/取消单
    def agree_refund(self, order_id):
        return self.__client.call("eleme.order.agreeRefund", {"orderId": order_id})

    # 不同意退单/取消单
    def disagree_refund(self, order_id, reason):
        return self.__client.call("eleme.order.disagreeRefund", {"orderId": order_id, "reason": reason})

    # 获取订单配送记录
    def get_delivery_state_record(self, order_id):
        return self.__client.call("eleme.order.getDeliveryStateRecord", {"orderId": order_id})

    # 批量获取订单最新配送记录
    def batch_get_delivery_states(self, order_ids):
        return self.__client.call("eleme.order.batchGetDeliveryStates", {"orderIds": order_ids})

    # 配送异常或者物流拒单后选择自行配送
    def delivery_by_self(self, order_id):
        return self.__client.call("eleme.order.deliveryBySelf", {"orderId": order_id})

    # 配送异常或者物流拒单后选择不再配送
    def no_more_delivery(self, order_id):
        return self.__client.call("eleme.order.noMoreDelivery", {"orderId": order_id})

