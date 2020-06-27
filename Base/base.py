from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver


class Base:
    def __init__(self):
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll=1):
        """
        定位单个元素方法
        :param loc: 元组 (By.xx,属性值)
        :param timeout: 搜索元素超时间
        :param poll: 搜索元素间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll=1):
        """
        定位一组元素方法
        :param loc: 元组 (By.xx,属性值)
        :param timeout:搜索元素超时间
        :param poll:搜索元素间隔
        :return:定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll=1):
        """
        点击元素方法
        :param loc: 元组 (By.xx,属性值)
        :param timeout: 搜索元素超时间
        :param poll: 搜索元素间隔
        :return:
        """
        self.search_ele(loc, timeout, poll).click()

    def send_ele(self, loc, text, timeout=5, poll=1):
        """
        输入方法
        :param loc: 元组 (By.ID,属性值) (By.CLASS_NAME,属性值) (By.XPATH,属性值)...
        :param text: 输入的文本内容
        :param timeout: 搜索元素超时间
        :param poll: 搜索元素间隔
        :return:
        """

        input_text = self.search_ele(loc, timeout, poll)
        input_text.clear()
        input_text.send_keys(text)
