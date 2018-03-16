# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from splinter import Browser
import time

## selenium
driver = webdriver.Chrome()
driver.get("http://www.dell.com/en-us/shop/dell-laptops/sc/laptops/xps-laptops")

videocard = driver.find_element_by_xpath('//div[@data-refiner="5712"]')
videocard.click() #點Videocards下拉選單

vccheckbox = driver.find_element_by_id('6149')
vccheckbox.click() #點Videocards的選項
time.sleep(5) #選擇要的顯卡,等一下網頁

titles = driver.find_elements_by_xpath('//span[@data-testid="configItemProductTitle"]')
for title in titles:
    print (title.text)

prices = driver.find_elements_by_xpath('//strong[@data-testid="psDellPrice"]')
for price in prices:
    print (price.text)



## splinter
#browser = Browser()
#browser.visit('http://www.dell.com/en-us/shop/dell-laptops/sc/laptops/xps-laptops')

#step1 = browser.find_by_xpath('//div[@data-refiner="5712"]').click()
#step2 = browser.find_by_id('6149').click()
#time.sleep(10)

#title = browser.find_by_xpath('//span[@data-testid="configItemProductTitle"]')
#price = browser.find_by_xpath('//strong[@data-testid="psDellPrice"]')

#for t in title:
#  print ("Product",t.text)

#for p in price:       #跑不
#  print ("Product",p.text)





#browser.fill('q', 'splinter - python acceptance testing for web applications')
#browser.find_by_css('.lsb').first.click()

#if browser.is_text_present('http://splinter.cobrateam.info'):
#    print ("Yes, the official website was found!")
#else:
#    print ("No, it wasn't found... We need to improve our SEO techniques")

#browser.quit()


#bw = Browser('firefox', options=firefox_options)
#bw.visit('http://www.dell.com/en-us/shop/dell-laptops/sc/laptops/xps-laptops?appliedRefinements=6149')

# 模擬行為
#selectSite = Select(browser.find_element_by_id("ctl15_ddlSite"))
#selectSite.select_by_value(cite)
#selectYear = Select(browser.find_element_by_id("ctl15_ddlYear"))
#selectYear.select_by_value(str(year))
#browser.find_element_by_id('ctl15_btnQuery').click()
