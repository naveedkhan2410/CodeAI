import requests
from bs4 import BeautifulSoup

url = "https://www.timesofindia.com"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

news_text = soup.find("p").get_text()
print(news_text)
