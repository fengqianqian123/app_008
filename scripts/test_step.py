import allure


class TestSetup:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("测试步骤名称")
    def test_001(self):
        """添加测试步骤"""
        allure.attach("测试步骤内容", "附件名字")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_002(self):
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_003(self):
        assert True