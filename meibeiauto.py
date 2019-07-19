from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
#启动浏览器
driver=webdriver.Chrome()
driver.get('http://aimeibei.sit.maiyafenqi.com/')
openid='js201901121451003'
driver.find_element_by_id("txtOpenID").send_keys(openid)
driver.find_element_by_id("txtShopID").send_keys('615')
driver.find_element_by_id("txtFaceID").send_keys('489')
driver.find_element_by_id("txtRateUuid").send_keys('5FFC321B5BA64950A3EE6E81F89FD31C')
