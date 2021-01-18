# ChromeDriver 可從以下網址下載，然後放到這個程式的資料夾內：
#https://sites.google.com/a/chromium.org/chromedriver/downloads



# 匯入函式庫
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime, csv



# 打開瀏覽器
driver = webdriver.Chrome(r'./chromedriver')  # mac 
driver.implicitly_wait(10)                # 如果瀏覽器頁面載入後，find_element_by_css_selector() 指定的元素未立刻出現，最多等待10秒，超時則視為錯誤。
driver.set_page_load_timeout(20)        # 如果瀏覽器最多等待頁面載入20秒，超時則視為錯誤。



# 前往aastock頁面
try:
    print("\n前往網址\n")
    driver.get('http://www.aastocks.com/tc/ltp/rtquote.aspx?symbol=00001')
except:
    pass

    
    
# 無限循環以下動作
while True:

    # 每個股票都做一次以下動作
    for share in ["00001", "00002", "00003", "00004", "00005"]:
    
        try:
            # 清空欄位，填入股票號碼，然後點擊按鈕前往股票頁面。
            print("\n前往股票 " + share)
            driver.switch_to.default_content()                # 轉回外層 iframe
            inputElem = driver.find_element_by_css_selector('[id="sb2-txtSymbol-aa"]')
            
            # 2020年12月更新: 我們發現新版網站 inputElem.clear() 有可能無法清除文字, 可改為用發送5個Backspace按鈕清除文字
            inputElem.send_keys(Keys.BACKSPACE * 5)         # 由於 Keys.BACKSPACE 型別為字串, 因此可直接用 *5 來把字串重複 5 次, 例如 "a" * 5 => "aaaaa"
            
            inputElem.send_keys(share)
            driver.find_element_by_css_selector('[id="sb2-btnSubmit"]').click()


            # 從股票頁面抓取資料
            print("從頁面抓取資料")
            driver.switch_to.frame("frameQuickQuote")        # 轉到股票內容iframe
            shareElem = driver.find_element_by_css_selector(
                '[class="abs txt_c ss3 cls font-num font-b"]'
            )
            data = []
            data.append( share )
            data.append( shareElem.text.strip().split('\n')[-1] )
            data.append( str(datetime.datetime.now())[0:19] )
            driver.switch_to.default_content()                # 轉回外層 iframe


            # 儲存資料到檔案
            # Append-Text 模式開啟檔案，如檔案不存在將自動新建
            print("儲存資料到檔案")
            with open(r"result.csv", "at", newline="") as f:

                # 以CSV格式寫入，定義CSV列順序
                writer = csv.writer(f)
                
                # 檢查檔案長度，如果檔案是空的，則寫入CSV列定義
                if f.tell() <= 0:
                    writer.writerow(["股票號", "現價", "抓取時間"])
                
                # 寫入資料
                writer.writerow(data)
                
            print("檔案寫入完成")

            
            # 每個股票之間短暫延時
            time.sleep(2)
            
        except Exception as e:
            # 如果頁面載入超時、或抓取資料出錯，則跳過這個股票。
            print("發生錯誤，跳過頁面：" + str(e))
            continue
            
            
    # 完成抓取所有股票資料，等待下次抓取
    print("\n完成抓取所有股票資料，下次抓取將在 60 秒後")
    time.sleep(60)
            
            
            
            
            
            
            
