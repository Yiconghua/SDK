# -*- coding: utf-8 -*-


# 经营体检
class DiagnosisService:

    __client = None

    def __init__(self, client):
        self.__client = client

    def get_shop_diagnosis(self, shop_id, date):
        """
        根据商户ID查询商户经营体检信息
        :param shopId:店铺ID
        :param date:体检日期(最多查到7天内的体检数据)
        """
        return self.__client.call("eleme.diagnosis.getShopDiagnosis", {"shopId": shop_id, "date": date})

    def get_shop_diagnosis_list(self, shop_ids, date):
        """
        根据多个商户ID批量查询商户经营体检信息
        :param shopIds:店铺ID集合
        :param date:体检日期(最多查到7天内的体检数据)
        """
        return self.__client.call("eleme.diagnosis.getShopDiagnosisList", {"shopIds": shop_ids, "date": date})

