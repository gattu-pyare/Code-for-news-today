import json
import requests
from bs4 import BeautifulSoup

url="https://inshorts.com/en/read/politics"

source_code = requests.get(url)
plain_text = source_code.text
soup =BeautifulSoup(plain_text, features="lxml")
# print(soup)
var=json.dumps(plain_text)
with open("code.txt","w") as f:
    f.write(var)

# this is not working as expected i dont kno whow to use this