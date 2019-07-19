from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains

import time
#启动浏览器
driver=webdriver.Chrome()
driver.get('http://sit-app.dzjk.infra/App/loginPage#')
#设置分辨率
driver.set_window_size(1280,1024)
#输入账号
username=driver.find_element_by_name('username').send_keys('jg02spl001')
#输入密码
password=driver.find_element_by_name('password').send_keys('111111')
#找到登录按钮
login=driver.find_element_by_class_name('button_login').click()
#任务中心
renwuzhongxin=driver.find_element_by_id('1DBCBC52791800014989140019301189').click()
#待处理列表
daifenpei=driver.find_element_by_xpath('//*[@id="nav"]/li[1]/ul/li[4]/a').click()
#启动
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
time.sleep(3)

#点击案件

b=str('datagrid-row-r1-1-')
#print(type(b))

for i  in range(0,20) :
    num = b + str(i)
#切换框架
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mainTab"]/div[2]/div/div/iframe'))

    diyige=driver.find_element_by_id(num)

#双击
    shuangxinanjian=ActionChains(driver).double_click(diyige).perform() #在此元素上双击
    time.sleep(5)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mainTab"]/div[2]/div[2]/div/iframe'))

    dianjishenpi=driver.find_element_by_xpath('//*[@id="applyInputTabs"]/div[1]/div[3]/ul/li[6]/a/span[1]').click()
    print('1点击审批意见菜单')
    time.sleep(3)

    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mainTab"]/div[2]/div[2]/div/iframe'))
    print('2跳到默认页')
    #选择结果
    driver.find_element_by_xpath('//*[@id="approveOpinionForm"]/div[1]/div[2]/table/tbody/tr[1]/td[2]/span[1]/input[1]').click()
    print('3开始选择')

    #选中结果
    driver.find_element_by_id('_easyui_combobox_4').click()
    print('4选中结果，通过')
    #提交
    driver.find_element_by_xpath('//*[@id="btnSubmit"]/span/span').click()
    print('5点击提交')

    #确认执行提交
    driver.find_element_by_xpath('/html/body/div[27]/div[2]/div[4]/a[1]/span/span').click()
    print('6确认提交')
    #等待
    time.sleep(10)
    #点击确认
    driver.find_element_by_xpath('/html/body/div[27]/div[2]/div[4]/a/span/span').click()
    print('7点击确认')

    print('等待10秒,重新开始',time.sleep(10))

# for i  in range(0,1) :
#
#          num=b+str(i)
#          print(num)
#          checkbox=driver.find_elements_by_id(num)
#
#          print(checkbox)
#          print (len(checkbox))
#          for a in checkbox :
#                  print(a.is_selected())
#                  print(a.click())





# #查询按钮，点击
# #browser.find_element_by_xpath('//*[@id="gridtb"]/a[1]/span').click()
# #勾选全选
# # daichuli=driver.find_elements_by_xpath('//*[@id="nav"]
#
# time.sleep(1)
# driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
# time.sleep(1)
#
# # checkbox=driver.find_elements_by_class_name('datagrid-row-index')
# # checkbox=driver.find_elements_by_xpath("//input[@type='checkbox']")
# b=str('datagrid-row-r1-1-')
# print(type(b))
#
# for i  in range(0,1) :
#
#         num=b+str(i)
#         print(num)
#         checkbox=driver.find_elements_by_id(num)
#
#         print(checkbox)
#         print (len(checkbox))
#         for a in checkbox :
#                 print(a.is_selected())
#                 print(a.click())
# time.sleep(2)
#
# driver.find_element_by_xpath('//*[@id="assignBtn"]/span/span').click()
# time.sleep(2)
# #选择
# driver.find_element_by_id('datagrid-row-r3-2-4').click()
#
# driver.find_element_by_xpath('//*[@id="dgtb"]/a[1]/span/span').click()
#
# #等待处理完成
# time.sleep(10)
# #
# driver.find_element_by_xpath('/html/body/div[9]/div[2]/div[4]/a/span/span').click()
# print('点击确认')
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