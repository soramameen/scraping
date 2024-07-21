from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
keyword = 'プログラミング'
url = 'https://www.youtube.com/'
driver.get(url)
time.sleep(10)

search = driver.find_element(By.ID, "ytd-searchbox")
search.send_keys(keyword)
search.submit()

time.sleep(10)

soup = BeautifulSoup(driver.page_source,"html.parser")
entries = soup.find_all("yt-formatted-string",attrs={"class":"style-scope ytd-video-renderer"})
# entries = recommend.find_all("yt-formatted-string",attrs={"id":"video-title"})

for entry in enumerate(entries):
    print(f'{entry.text}')
    
    
driver.quit()
