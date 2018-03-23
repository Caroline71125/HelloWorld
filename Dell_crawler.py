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
videocardID = ['']
vccheckbox = driver.find_element_by_id('6149')
gpuname = vccheckbox.text.encode('utf-8').split('® ')[2]

print(vccheckbox.text)
vccheckbox.click() #點Videocards的選項
time.sleep(5) #等一下網頁

test = {}
namelist = list()
pricelist = list()

names = driver.find_elements_by_xpath('//span[@data-testid="configItemProductTitle"]')
for name in names:
    namelist.append(name.text)
    #test['title'] = title.text
    #print (title.text)



prices = driver.find_elements_by_xpath('//strong[@data-testid="psDellPrice"]')
for price in prices:
    pricelist.append(price.text)
    #test['price'] = price.text
    #print (price.text)


#print(titlelist)
#print(pricelist)



test['name'] = namelist
test['price'] = pricelist

print(test)

#vctype = [6149, 6151, 6153, 6157, 6159]

##### 3/23 #####
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
videocardID = ['']
vccheckbox = driver.find_element_by_id('6149')
gpuname = vccheckbox.text.encode('utf-8').split('® ')[2]
print(gpuname, type(gpuname))
vccheckbox.click() #點Videocards的選項
time.sleep(5) #等一下網頁



headers=['productName', 'productPrice', 'gpuName', 'gpuType', 'createDate', 'modifyDate']
test = {}
for h in headers:
    test[h]=[]

#prices = driver.find_elements_by_xpath('//strong[@data-testid="psDellPrice"]')
#for price in prices:
#    pricelist.append(price.text)
    
names = driver.find_elements_by_xpath('//span[@data-testid="configItemProductTitle"]')

for name in names:
    test['productName'].append(name.text)
    test['gpuName'].append(gpuname)    
    
#fruits = ['banana', 'apple',  'mango']
#for h in fruits:    
#    test['name'].append(h)
#    test['price'].append(gpuname)
    
print(test)


##### 3/23 #####
#class Product():
# def __init__(self, title, price, displaysize):
#  self.title = title
#  self.price = price
#  self.displaysizes = displaysizes
#a = Product("")  #建立一個名叫dog的Animal實體(物件)
#print(a.name)

#//*[@id="ProductStackContainer"]/div[1]/div/div[4]/div[2]/div[1]/div/div/p/span


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
