# 匯入 selenium 模組
from selenium import webdriver

########################## aastock 股票評論新聞 ##########################

# 打開瀏覽器
driver = webdriver.Chrome(r'./chromedriver.exe')		# For Windows
# driver = webdriver.Chrome(r'./chromedriver')			# For Mac

# 前往頁面
driver.get('http://www.aastocks.com/')

# 步驟1: 滑鼠移動到「評論及研究」，然後移動到「股票評論」，最後點擊「股票評論」

# elem1 為「評論及研究」元素
elem1 = driver.find_element_by_css_selector(
    '#topPanel-menu a[href="/tc/stocks/news/commentary-overview.aspx"]'
)
# elem2 為「股票評論」元素
elem2 = driver.find_element_by_css_selector(
    '#topPanel-menu a[href="/tc/stocks/news/commentary.aspx"]'
)
# 建立 ActionChains
action = webdriver.ActionChains(driver)
# 滑鼠移動到「評論及研究」
action.move_to_element(elem1).perform()
# 滑鼠移動到「股票評論」
action.move_to_element(elem2).perform()
# 滑鼠點擊
action.click().perform()


# ActionChains 簡化寫法，一次過執行所有動作，每行須以\結尾
webdriver.ActionChains(driver)          \
    .move_to_element(elem1)             \
    .move_to_element(elem2)             \
    .click()                            \
    .perform()

# 步驟2: 選取「機構」
driver.find_element_by_css_selector(
	'#ddlSearchType > option[value="2"]'
).click()

# 步驟3: 點擊「所有機構」
driver.find_element_by_css_selector(
	'#InstitutionTable .tab_C[title="所有機構"]'
).click()

# 步驟4: 取得所有新聞標題
elems = driver.find_elements_by_css_selector('.newshead4 a')
data = []
for i in elems:
	data.append( i.get_attribute('href') )
print( data )
	
# 步驟5: 點擊「下一頁」
driver.find_elements_by_css_selector(
	'table.imglin'
)[-1].click()


########################## 檔案下載 - 方法1 ##########################

# 前往頁面
driver.get('https://chromedriver.storage.googleapis.com/index.html?path=2.41/')

# 點擊連結下載檔案
driver.find_element_by_partial_link_text('win32.zip').click()

########################## 檔案下載 - 方法2 ##########################

# 匯入 urllib.request 模組
import urllib.request

# 下載檔案
urllib.request.urlretrieve(
	'https://chromedriver.storage.googleapis.com/2.41/chromedriver_win32.zip', 
	'chromedriver.zip'
)

# 下載圖片
urllib.request.urlretrieve(
	'http://plib.aastocks.com/aafnnews/image/medialib/20180112150828192_s.jpg', 
	'1.jpg'
)

########################## 存取登入資料 ChromeOptions() ##########################

c = webdriver.ChromeOptions()
c.add_argument( r"user-data-dir=C:\Users\User\Desktop\test" )
driver = webdriver.Chrome( r"./chromedriver.exe", options=c )		# For Windows
# driver = webdriver.Chrome( r"./chromedriver", options=c )		# For Mac

# 前往頁面
driver.get('http://oursogo.com/')


# 關閉頁面
driver.close()


	




