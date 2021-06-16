from selenium.webdriver.common.by import By
from utils.page_base import PageBase

class PageConcat(PageBase):
    def __init__(self,driver):
        self.driver=driver

    #元素特征
    loc_jiahao=By.ID,"com.android.contacts:id/floating_action_button"
    loc_bendibaocun=By.XPATH,"text,本地保存,1"
    loc_name=By.XPATH,"text,姓名,1"
    loc_phone=By.XPATH,"text,电话,1"
    loc_company=By.XPATH,"text,公司,1"
    loc_website=By.XPATH,"text,网站,1"
    loc_fanhuijiantou=By.CLASS_NAME,"android.widget.ImageButton"

    #实现业务函数
    def click_jiahao(self):
        self.click(loc=PageConcat.loc_jiahao)

    # 2.点击“本地保存”按钮
    def click_bendibaocun(self):
        self.click(loc=PageConcat.loc_bendibaocun)

    # 3.输入姓名：张三
    def input_name(self,name):
        self.input_text(loc=PageConcat.loc_name,text=name)

    # 4.输入电话：13760453683
    def input_phone(self,phone):
        self.input_text(loc=PageConcat.loc_phone,text=phone)

    # 5.输入公司：
    def input_company(self,company):
        self.input_text_scroll(loc=PageConcat.loc_company,data=company)

    # 6.输入网址
    def input_website(self,website):
        self.input_text_scroll(loc=PageConcat.loc_website,data=website)

    #7.点击返回箭头
    def click_fanhuijiantou(self):
        self.click(loc=PageConcat.loc_fanhuijiantou)