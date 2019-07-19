from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains

import time
#启动浏览器
driver=webdriver.Chrome()
driver.get('http://sit-app.dzjk.infra/App/loginPage#')

driver.set_window_size(1280,800)  # 分辨率 1280*800

driver.set_window_size(1280,1024) # 分辨率 1280*800

driver.close()
