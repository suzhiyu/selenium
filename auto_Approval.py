from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
#启动浏览器
driver=webdriver.Chrome()
driver.get('http://sit-app.dzjk.infra/App/loginPage#')

#设置分辨率
driver.set_window_size(1280,1024)  # 分辨率 1280*1024

#输入账号
username=driver.find_element_by_name('username').send_keys('jg02spl001')
#输入密码
password=driver.find_element_by_name('password').send_keys('111111')
#找到登录按钮
login=driver.find_element_by_class_name('button_login').click()
#任务中心
renwuzhongxin=driver.find_element_by_id('1DBCBC52791800014989140019301189').click()
print('1任务中心')
#待分配列表
daifenpei=driver.find_element_by_xpath('//*[@id="nav"]/li[1]/ul/li[2]/a').click()
print('2待分配')
#查询按钮，点击
#browser.find_element_by_xpath('//*[@id="gridtb"]/a[1]/span').click()
#勾选全选
# daichuli=driver.find_elements_by_xpath('//*[@id="nav"]

time.sleep(1)
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
print('切换ifanme')
time.sleep(1)

# checkbox=driver.find_elements_by_class_name('datagrid-row-index')
# checkbox=driver.find_elements_by_xpath("//input[@type='checkbox']")
b=str('datagrid-row-r1-1-')
print(type(b))

for i  in range(0,20) :

        num=b+str(i)
        print(num)
        checkbox=driver.find_elements_by_id(num)

        print(checkbox)
        print (len(checkbox))
        for a in checkbox :
                print(a.is_selected())
                print(a.click())
time.sleep(2)

driver.find_element_by_xpath('//*[@id="assignBtn"]/span/span').click()
time.sleep(2)
#选择
driver.find_element_by_id('datagrid-row-r3-2-4').click()
print('分配处理人')
driver.find_element_by_xpath('//*[@id="dgtb"]/a[1]/span/span').click()
print('确认')
#等待处理完成
time.sleep(10)
#
driver.find_element_by_xpath('/html/body/div[9]/div[2]/div[4]/a/span/span').click()
print('点击确认')
# #任务中心
# renwuzhongxin=driver.find_element_by_xpath('exp').click()
# time.sleep(2)
#
# #待处理
# driver.find_element_by_xpath('//*[@id="nav"]/li[1]/ul/li[4]/a').is_selected()
#
# driver.find_element_by_id('datagrid-row-r1-1-0').click()
#
# time.sleep(5)
# #找到iframe
# driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
#
# #点击审批
# driver.find_element_by_xpath('//*[@id="applyInputTabs"]/div[1]/div[3]/ul/li[6]/a/span[1]').click()
#
#