from urllib import response
from wsgiref import headers
import requests
from bs4 import BeautifulSoup

header = {"user-agent" : "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)"}

link = "https://browser-info.ru/"
response = requests.get(link, headers = header).text
soup = BeautifulSoup(response, features="html.parser")
block = soup.find("div", id = "tool_padding")


#Check JS
check_js = block.find("div", id = "javascript_check")
status_js = check_js.find_all("span")[1].text
result_js = f"javascript: {status_js}"

#Check flash

check_flash = block.find("div", id = "flash_version")
status_flash = check_flash.find_all("span")[1].text
result_flash = f"flash: {status_flash}"

#Check user-agent

check_ua = block.find("div", id = "user_agent").text

print(result_js, result_flash, check_ua, sep = "\n")