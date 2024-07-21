from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv


# サービスオブジェクトを作成
service = Service(ChromeDriverManager().install())

# WebDriverの初期化
driver = webdriver.Chrome(service=service)

# amazonのページを開く
url = 'https://www.amazon.co.jp/primeday?ref_=nav_cs_td_pd_dt_cr&discounts-widget=%2522%257B%255C%2522state%255C%2522%253A%257B%255C%2522refinementFilters%255C%2522%253A%257B%257D%257D%252C%255C%2522version%255C%2522%253A1%257D%2522'
# keyword = "スクレイピング"
driver.get(url)

# 3秒待機
time.sleep(5)
soup = BeautifulSoup(driver.page_source,"html.parser")
entries = soup.find_all("li",{"class":"a-carousel-card _ZGlzY_desktopCardCarouselElement_1c8nD"})
prace_list = []
prace_list.append(['割引','商品名','価格'])
for entry in entries:
    entry_name = entry.find("span",{"class","a-truncate-cut"})
    entry_price = entry.find("span",{"class","a-price-whole"})
    cut_price = entry.find("span",{"class":"a-size-mini"})
    name = entry_name.text
    price = entry_price.text
    cut = cut_price.text
    price_int = int(price.replace(',', '').replace('¥', '').strip())
    product_name = name.encode('shift_jis', errors='ignore').decode('shift_jis')

    prace_list.append([f'{cut}',product_name,int(price_int)])
    print(f'{entry_name.text}:{entry_price.text}円')    
    
with open("output3.csv","w",encoding="Shift_JIS",newline='') as file:
    writer = csv.writer(file,lineterminator="\n")
    writer.writerows(prace_list)
driver.quit()

