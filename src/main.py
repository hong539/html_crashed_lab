import os
import requests
from bs4 import BeautifulSoup

url = os.environ['url']

response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")

temp = soup.find_all("div")

print(temp)