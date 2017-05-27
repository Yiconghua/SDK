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

    def confirm_order_lite(self, order_id):
        """
        确认订单(推荐)
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.confirmOrderLite", {"orderId": order_id})

    def confirm_order(self, order_id):
        """
        确认订单
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.confirmOrder", {"orderId": order_id})

    def cancel_order_lite(self, order_id, type, remark):
        """
        取消订单(推荐)
        :param orderId:订单Id
        :param type:取消原因
        :param remark:备注说明
        """
        return self.__client.call("eleme.order.cancelOrderLite", {"orderId": order_id, "type": type, "remark": remark})

    def cancel_order(self, order_id, type, remark):
        """
        取消订单
        :param orderId:订单Id
        :param type:取消原因
        :param remark:备注说明
        """
        return self.__client.call("eleme.order.cancelOrder", {"orderId": order_id, "type": type, "remark": remark})

    def agree_refund_lite(self, order_id):
        """
        同意退单/同意取消单(推荐)
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.agreeRefundLite", {"orderId": order_id})

    def agree_refund(self, order_id):
        """
        同意退单/同意取消单
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.agreeRefund", {"orderId": order_id})

    def disagree_refund_lite(self, order_id, reason):
        """
        不同意退单/不同意取消单(推荐)
        :param orderId:订单Id
        :param reason:商家不同意退单原因
        """
        return self.__client.call("eleme.order.disagreeRefundLite", {"orderId": order_id, "reason": reason})

    def disagree_refund(self, order_id, reason):
        """
        不同意退单/不同意取消单
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

    def delivery_by_self_lite(self, order_id):
        """
        配送异常或者物流拒单后选择自行配送(推荐)
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.deliveryBySelfLite", {"orderId": order_id})

    def delivery_by_self(self, order_id):
        """
        配送异常或者物流拒单后选择自行配送
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.deliveryBySelf", {"orderId": order_id})

    def no_more_delivery_lite(self, order_id):
        """
        配送异常或者物流拒单后选择不再配送(推荐)
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.noMoreDeliveryLite", {"orderId": order_id})

    def no_more_delivery(self, order_id):
        """
        配送异常或者物流拒单后选择不再配送
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.noMoreDelivery", {"orderId": order_id})

    def received_order_lite(self, order_id):
        """
        订单确认送达(推荐)
        :param orderId:订单ID
        """
        return self.__client.call("eleme.order.receivedOrderLite", {"orderId": order_id})

    def received_order(self, order_id):
        """
        订单确认送达
        :param orderId:订单ID
        """
        return self.__client.call("eleme.order.receivedOrder", {"orderId": order_id})

    def reply_reminder(self, remind_id, type, content):
        """
        回复催单
        :param remindId:催单Id
        :param type:回复类别
        :param content:回复内容,如果type为custom,content必填,回复内容不能超过30个字符
        """
        return self.__client.call("eleme.order.replyReminder", {"remindId": remind_id, "type": type, "content": content})

    def get_commodities(self, order_id):
        """
        获取指定订单菜品活动价格.
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.getCommodities", {"orderId": order_id})

    def mget_commodities(self, order_ids):
        """
        批量获取订单菜品活动价格
        :param orderIds:订单Id列表
        """
        return self.__client.call("eleme.order.mgetCommodities", {"orderIds": order_ids})

    def get_refund_order(self, order_id):
        """
        获取订单退款信息
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.getRefundOrder", {"orderId": order_id})

    def mget_refund_orders(self, order_ids):
        """
        批量获取订单退款信息
        :param orderIds:订单Id列表
        """
        return self.__client.call("eleme.order.mgetRefundOrders", {"orderIds": order_ids})

    def cancel_delivery(self, order_id):
        """
        取消呼叫配送
        :param orderId:订单Id
        """
        return self.__client.call("eleme.order.cancelDelivery", {"orderId": order_id})

    def call_delivery(self, order_id, fee):
        """
        呼叫配送
        :param orderId:订单Id
        :param fee:小费,1-8之间的整数
        """
        return self.__client.call("eleme.order.callDelivery", {"orderId": order_id, "fee": fee})

    def get_unreply_reminders(self, shop_id):
        """
        获取店铺未回复的催单
        :param shopId:店铺id
        """
        return self.__client.call("eleme.order.getUnreplyReminders", {"shopId": shop_id})

    def get_unprocess_orders(self, shop_id):
        """
        查询店铺未处理订单
        :param shopId:店铺id
        """
        return self.__client.call("eleme.order.getUnprocessOrders", {"shopId": shop_id})

    def get_cancel_orders(self, shop_id):
        """
        查询店铺未处理的取消单
        :param shopId:店铺id
        """
        return self.__client.call("eleme.order.getCancelOrders", {"shopId": shop_id})

    def get_refund_orders(self, shop_id):
        """
        查询店铺未处理的退单
        :param shopId:店铺id
        """
        return self.__client.call("eleme.order.getRefundOrders", {"shopId": shop_id})

    def get_all_orders(self, shop_id, page_no, page_size, date):
        """
        查询全部订单
        :param shopId:店铺id
        :param pageNo:页码。取值范围:大于零的整数最大限制为100; 默认值:1
        :param pageSize:每页获取条数。默认值20，最小值1，最大值50。
        :param date:日期,默认当天,格式:yyyy-MM-dd
        """
        return self.__client.call("eleme.order.getAllOrders", {"shopId": shop_id, "pageNo": page_no, "pageSize": page_size, "date": date})

