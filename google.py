from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# サービスオブジェクトを作成
service = Service(ChromeDriverManager().install())

# WebDriverの初期化
driver = webdriver.Chrome(service=service)

# Googleのページを開く
url = 'https://www.google.com/'
keyword = "スクレイピング"
driver.get(url)

# 3秒待機
time.sleep(3)

# 検索ボックスを見つけてキーワードを入力
search = driver.find_element(By.NAME, "q")
search.send_keys(keyword)
search.submit()
# 5秒待機して結果を表示
time.sleep(5)
soup = BeautifulSoup(driver.page_source,"html.parser")
titles = soup.find_all("h3")

for index, title in enumerate(titles):
    print(f'{index+1}:{title.text}')

# 5秒待機して結果を表示
# time.sleep(5)



# ドライバーを終了
driver.quit()
