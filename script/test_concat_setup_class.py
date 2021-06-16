import pytest,os,sys,time,allure
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from config.base_driver import init_driver
from page.page_concat import PageConcat
from utils.YamlUtils import yaml_data_with_file1



class TestConcat(object):
    def setup_class(self):
        self.driver=init_driver()
        self.page_concat=PageConcat(self.driver);

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()


    @allure.step(title="测试登录UI的主流程")
    @pytest.mark.parametrize("data", yaml_data_with_file1("./data/data_concat.yaml", "test_concat_001"))
    def test_concat_001(self,data):
        #部分1：接收测试数据
        name=data["name"]
        phone=data["phone"]
        company=data["company"]
        website=data["website"]
        key=data["key"]
        #部分2：业务步骤
        allure.attach("","步骤1：点击“+”号")
        #1.点击“+”号
        self.page_concat.click_jiahao();
        #2.点击“本地保存”按钮
        # allure.attach("", "步骤2：点击“本地保存”")
        # self.page_concat.click_bendibaocun();
        #3.输入姓名：张三
        allure.attach("", "步骤3：输入账号:"+name)
        self.page_concat.input_name(name);
        #4.输入电话：13760453683
        allure.attach("", "步骤4：输入手机:" +phone)
        self.page_concat.input_phone(phone);
        #5.输入公司：
        allure.attach("", "步骤5：输入公司:" + company)
        self.page_concat.input_company(company)
        #6.输入网址
        allure.attach("", "步骤6：输入网址:" + website)
        self.page_concat.input_website(website)
        #7.点击返回箭头
        allure.attach("", "步骤7：点击返回箭头")
        self.page_concat.click_fanhuijiantou();
        #部分3：断言
        #方法1
        ret=self.page_concat.is_toast_exist(message="已保存",is_screenshot=True,screenshot_name=key)
        #把截到的截图嵌入到Allure测试报告
        allure.attach(open('./screen/' + key + '.png', 'rb').read(), "步骤8：本次截图", allure.attachment_type.PNG)
        # 8.还原到业务刚开始的UI
        self.driver.keyevent(4);
        time.sleep(2)
        assert ret
        #方法2
        # ret=self.page_concat.is_loc_exist((By.XPATH,"text,"+name+",1"))
        # assert ret
