# -*- coding: utf-8 -*-


# 商户信用分服务
class ShopcreditscoreService:

    __client = None

    def __init__(self, client):
        self.__client = client

    def batch_query_shop_credit_scores(self, shop_ids):
        """
        连锁店根据商户ID集合批量查询商户信用分信息
        :param shopIds:商户ID集合
        """
        return self.__client.call("eleme.shopCreditScore.chain.batchQueryShopCreditScores", {"shopIds": shop_ids})

    def batch_query_shop_equity_rules(self, shop_ids):
        """
        连锁店根据商户ID集合批量查询店铺权益规则
        :param shopIds:商户ID集合
        """
        return self.__client.call("eleme.shopCreditScore.chain.batchQueryShopEquityRules", {"shopIds": shop_ids})

    def batch_query_shop_punish_rules(self, shop_ids):
        """
        连锁店根据商户ID集合批量查询店铺扣罚规则
        :param shopIds:商户ID集合
        """
        return self.__client.call("eleme.shopCreditScore.chain.batchQueryShopPunishRules", {"shopIds": shop_ids})

    def batch_query_shop_credit_score_records(self, shop_ids):
        """
        连锁店根据商户ID集合批量查询查询商户信用分变更记录
        :param shopIds:商户ID集合
        """
        return self.__client.call("eleme.shopCreditScore.chain.batchQueryShopCreditScoreRecords", {"shopIds": shop_ids})

    def get_shop_credit_score(self, shop_id):
        """
        根据商户ID查询商户信用分信息
        :param shopId:商户ID
        """
        return self.__client.call("eleme.shopCreditScore.single.getShopCreditScore", {"shopId": shop_id})

    def get_shop_equity_rules(self, shop_id):
        """
        根据商户ID查询店铺权益规则
        :param shopId:商户ID
        """
        return self.__client.call("eleme.shopCreditScore.single.getShopEquityRules", {"shopId": shop_id})

    def get_shop_punish_rules(self, shop_id):
        """
        根据商户ID查询店铺扣罚规则
        :param shopId:商户ID
        """
        return self.__client.call("eleme.shopCreditScore.single.getShopPunishRules", {"shopId": shop_id})

    def get_shop_credit_score_record(self, shop_id):
        """
        查询商户信用分变更记录
        :param shopId:商户ID
        """
        return self.__client.call("eleme.shopCreditScore.single.getShopCreditScoreRecord", {"shopId": shop_id})

