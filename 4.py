import requests
from bs4 import BeautifulSoup
url="https://b.hatena.ne.jp/"

response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
entries = soup.find("section",attrs={"class":"entrylist-unit"})
# entries = popular.find_all("h3",attrs={"class":"entrylist-contents-title"})
# goods = popular.find_all("span",attrs={"class":"entrylist-contents-users"})

for index,entry in enumerate(entries):
        title_tag = entry.find("h3",attrs={"class":"entrylist-contents-title"})
        title = title_tag.find("a").get("title")
        user_tag = entry.find("span",attrs={"class":"entrylist-contents-users"})
        user = user_tag.get_text().strip()
        print(f"{user}:{title}")
        