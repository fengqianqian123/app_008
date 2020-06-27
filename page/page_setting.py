from Base.base import Base
from page.page_elements import PageElements


class SettingPage(Base):

    def __init__(self):
        super().__init__()

    def click_search_btn(self):
        self.click_ele(PageElements.search_btn_id)







