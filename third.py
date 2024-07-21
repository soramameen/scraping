import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8'

response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
today = soup.find("div",attrs={"id":"on_this_day"})
# print(today)

entries = today.find_all("li")
today_list = []
for index,entry in enumerate(entries):
    today_text = entry.get_text().replace("（","(").replace("）",")")
    pattern = r'\((\d+)年\)'
    match = re.search(pattern,today_text)
    if match:
        
        today_list.append([index,entry.get_text(),match.group(1)])
    else:
        today_list.append([index,entry.get_text()])

with open("output2.csv","w",encoding="Shift_JIS",newline='') as file:
    writer = csv.writer(file,lineterminator="\n")
    writer.writerows(today_list)