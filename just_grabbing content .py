import requests
from bs4 import BeautifulSoup

source_code = requests.get("https://inshorts.com/en/read/spacex")
plain_text = source_code.text
soup =BeautifulSoup(plain_text, features="lxml")
name = []
file = open("code.txt","w")
for link in soup.findAll('li', {"class": "active-category"}):
    file.writelines(f"{link} \n ")

#after this i used cut command in linux to get the li tags


file.close()
# print(name)