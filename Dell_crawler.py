# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from splinter import Browser


browser = Browser()
browser.visit('http://www.dell.com/en-us/shop/dell-laptops/sc/laptops/xps-laptops')

s1 = browser.find_by_xpath('//div//a[@class="btn btn-default dropdown-toggle col-xs-12 accessories-anav-dropdown-styling refiner-title"]')
s2 = browser.find_by_css('.dropdown-toggle')
print ("s1", s1)
print ("s2", s2)


#browser.fill('q', 'splinter - python acceptance testing for web applications')
#browser.find_by_css('.lsb').first.click()

#if browser.is_text_present('http://splinter.cobrateam.info'):
#    print ("Yes, the official website was found!")
#else:
#    print ("No, it wasn't found... We need to improve our SEO techniques")

browser.quit()


#bw = Browser('firefox', options=firefox_options)
#bw.visit('http://www.dell.com/en-us/shop/dell-laptops/sc/laptops/xps-laptops?appliedRefinements=6149')

# 模擬行為
#selectSite = Select(browser.find_element_by_id("ctl15_ddlSite"))
#selectSite.select_by_value(cite)
#selectYear = Select(browser.find_element_by_id("ctl15_ddlYear"))
#selectYear.select_by_value(str(year))
#browser.find_element_by_id('ctl15_btnQuery').click()
