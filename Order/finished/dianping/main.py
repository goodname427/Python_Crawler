from selenium import webdriver

options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Edge(options=options)      # Edge浏览器
driver.get('https://www.dianping.com/beijing/ch10/g110')
input()
