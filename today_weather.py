import requests
from bs4 import BeautifulSoup

url= 'https://weather.yahoo.co.jp/weather/jp/33/6610/33101.html'
response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

div_today = soup.find("div",{"id":"yjw_pinpoint_today"})
imgs_today = div_today.find_all("img")
time = 0
print('今日の天気を3時間ごとでお知らせします')
for entry in imgs_today:
    alt_value = entry.get('alt')
    print(f'{time}時:{alt_value}')
    time += 3

