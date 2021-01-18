# ChromeDriver 可從以下網址下載，然後放到這個程式的資料夾內：
# https://sites.google.com/a/chromium.org/chromedriver/downloads




###############   實戰程式會用到的函式   ###############


# 匯入 selenium 函式庫
from selenium import webdriver



# 打開瀏覽器
driver = webdriver.Chrome(r'./chromedriver.exe')     # windows



# 前往網址
driver.get(r'http://www.aastocks.com/tc/ltp/rtquote.aspx?symbol=00001')



# 取得股票輸入框元素
inputElem = driver.find_element_by_css_selector('[id="sb2-txtSymbol-aa"]')                                           



# 清除輸入框文字
# 2020年12月更新: 我們發現新版網站 inputElem.clear() 有可能無法清除文字, 可改為用發送5個Backspace按鈕清除文字
# inputElem.clear()
from selenium.webdriver.common.keys import Keys     # 匯入特殊字元
inputElem.send_keys(Keys.BACKSPACE * 5)              # 由於 Keys.BACKSPACE 型別為字串, 因此可直接用 *5 來把字串重複 5 次, 例如 "a" * 5 => "aaaaa"



# 輸入框輸入文字
inputElem.send_keys('00001')



# 點擊前往按鈕
driver.find_element_by_css_selector('[id="sb2-btnSubmit"]').click()



# 切換至 iframe 頁框
driver.switch_to.frame("frameQuickQuote")



# 取得股票現價
priceElem = driver.find_element_by_css_selector('[class="abs txt_c ss3 cls font-num font-b"]')
priceElem.text                              # 利用 .text 取得文字內容
priceElem.text.strip().split('\n')[-1]      # 利用 .text 取得文字內容，移除前後空白字元，和股價走勢箭頭



# 切換回到最外層頁框
driver.switch_to.default_content()





###############   更多 Selenium 函數   ###############


# 一次返回多個元素 find_elements_by_css_selector()
selectElem = driver.find_elements_by_css_selector('.s1')
selectElem[0].text
selectElem[1].text
selectElem[2].text




# 輸入特殊按鍵
# 例子：在輸入框中輸入股票號後，再輸入ENTER
from selenium.webdriver.common.keys import Keys 
inputElem = driver.find_element_by_css_selector('[id="sb2-txtSymbol-aa"]')
inputElem.clear()
inputElem.send_keys('00002')                                              
inputElem.send_keys(Keys.ENTER)
                           



# 取得元素 HTML attributes
attrElem = driver.find_element_by_css_selector('.recentQuoteRows a')
attrElem.get_attribute('href')          # 取得 a 的連結內容



# 取得元素 HTML 代碼
attrElem = driver.find_element_by_css_selector('.recentQuoteRows')
attrElem.get_attribute('outerHTML')           #包含元素內的HTML，包括元素自身                            
attrElem.get_attribute('innerHTML')           #包含元素內的HTML，不包括元素自身                    




# 如果瀏覽器頁面載入後，find_element_by_*() 指定的元素未立刻出現，最多等待10秒，超時則拋出例外 Exception。
driver.implicitly_wait(5)
driver.get(r'http://www.aastocks.com/tc/ltp/rtquote.aspx?symbol=00020')
attrElem = driver.find_element_by_css_selector('aaaaaaaa')



# 瀏覽器最多等待頁面載入20秒，超時則拋出例外 Exception。
driver.set_page_load_timeout(5)



# 重新整理頁面
driver.refresh()



# 拍攝屏幕
driver.save_screenshot('result.png')



# 運行 Javascript 代碼 ， window.open(''); 為打開新分頁代碼 
driver.execute_script( "window.open('');" )



# 切換至最後一個分頁
driver.switch_to.window( driver.window_handles[0] )


# 控制分頁前往網址
driver.get('https://google.com')


# 關閉分頁
driver.close()


# 關閉瀏覽器
driver.quit()




           

