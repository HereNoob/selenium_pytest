from page.webpage import WebPage, sleep
from common.readelement import Element

search = Element('search')

class SearchPage(WebPage):
    """搜索类"""
    def input_search(self, content):
        """输入搜索内容"""
        self.input_text(search['搜索框'], txt=content)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        return [x.text for x in self.find_elements(search['候选'])]

    def click_search(self):
        """点击搜索"""
        self.click_ele(search['搜索按钮'])
        