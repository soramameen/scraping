import requests
from bs4 import BeautifulSoup

url='https://www.ufret.jp/'
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
popular = soup.find("div",{"class":"list-group"})

entries = popular.find_all("a")

for index,entry in enumerate(entries):
    title = entry.find("strong").get_text()
    print(f'{index+1}:{title}')