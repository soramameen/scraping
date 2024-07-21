from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random

# ユーザーエージェントを設定
options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

# サービスオブジェクトを作成
service = Service(ChromeDriverManager().install())

# WebDriverの初期化
driver = webdriver.Chrome(service=service, options=options)

# URLにアクセス
url = 'https://jp.trip.com/flights/hanoi-to-osaka/tickets-han-osa?dcity=han&acity=osa&ddate=2024-09-25&rdate=2024-09-28&flighttype=ow&class=y&lowpricesource=searchform&quantity=1&searchboxarg=t'
driver.get(url)

# ランダムな待機時間（3～10秒）を設定
time.sleep(random.uniform(3, 10))

# ページのHTMLを取得してBeautifulSoupで解析
soup = BeautifulSoup(driver.page_source, "html.parser")
list_div = soup.find("div", {"class": "m-main-list"})
entries = list_div.find_all("span", {"class": "ThemeColor8 f-20 o-price-flight_4ST no-cursor_4SU"})

for entry in entries:
    print(entry.get_text())

# ドライバーを終了
driver.quit()
