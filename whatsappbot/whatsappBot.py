# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:28:11 2020

@author: admin
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime, csv

driver = webdriver.Chrome(r'./chromedriver.exe') 

#driver.implicitly_wait(10)                # 如果瀏覽器頁面載入後，find_element_by_css_selector() 指定的元素未立刻出現，最多等待10秒，超時則視為錯誤。
driver.set_page_load_timeout(20)        # 如果瀏覽器最多等待頁面載入20秒，超時則視為錯誤。

try:
    print("\n前往網址\n")
    driver.get('https://web.whatsapp.com/')
    time.sleep(15)
except:
    pass


for x in range(20):
    user_name = '備忘錄'
    text_content = "乖乖辛苦你 \uE418"
    button_name = "_2Ujuu"
    #備忘錄 
    #M 小姐 :emoji' u'\ue007 \ud83d\udc4d
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
    #user = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[16]/div/div/div[2]/div[1]/div[1]/span')
    user.click()
    
    #message_box= 'Srlyw'
    message = driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]')
    message.send_keys(text_content)
    print("\n打到字\n")
    
    message_button = driver.find_element_by_xpath('//span[@data-testid="send"][@data-icon="send"]')
    message_button.click()
    print("\nbutton\n")

       
    
#//*[@id="main"]/footer/div[1]/div[2]/div/div[2]

#//*[@id="main"]/footer/div[1]/div[2]/div/div[1]
#_1awRl copyable-text selectable-text

"""
<button class="_2Ujuu"><span data-testid="send" data-icon="send" class="">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
<path fill="currentColor" d="M1.101 21.757L23.8 12.028 1.101 2.3l.011 7.912 13.623 1.816-13.623 1.817-.011 7.912z">
</path></svg></span></button>
"""