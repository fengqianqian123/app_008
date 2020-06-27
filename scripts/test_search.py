import pytest
from Base.driver import Driver
from Base.page import Page


class TestSearch:

    def teardown_class(self):
        # 退出driver
        Driver.quit_app_driver()

    @pytest.fixture(scope="class")
    def click_search_btnon(self):
        """点击搜索按钮 并且 点击一次"""
        Page.get_searchPage().click_search_btn()

    @pytest.mark.parametrize("search_data,exp_data", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search_text(self, click_search_btnon, search_data, exp_data):
        """
        搜索测试方法
        :param search_data: 输入内容
        :param exp_data: 预期结果
        :return:
        """
        Page.get_searchPage().search_text(search_data)

        assert exp_data in Page.get_searchPage().get_search_result()
