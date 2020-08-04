import json
import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

with open('account.json', 'rt', encoding='UTF8') as json_file:
    json_data = json.load(json_file)
    id = json_data["id"]
    pw = json_data["pw"]

link = input("Please typing url what you want to download : ")
file = input("Please drop down Torrent File (or typing it's physical directory directions) : ")

login_session = "https://your-nas-domain/webapi/auth.cgi?api=SYNO.API.Auth&version=2&method=login&account=%s&passwd=%s&session=DownloadStation&format=cookie" % (id, pw)
download_task = "https://your-nas-domain/webapi/DownloadStation/task.cgi?api=SYNO.DownloadStation.Task&version=1&method=list&format=cookie"

options = webdriver.ChromeOptions()
options.add_argument('log-level=2')
options.add_argument('window-size=1280x720')
options.add_argument('headless')
options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(login_session)
delay = 2
driver.implicitly_wait(delay)

driver.get(download_task)
delay = 2
title = driver.find_element_by_tag_name("pre").text
data = json.loads(title)
with open('list.json', 'w', encoding='utf-8') as make_file:
    json.dump(title, make_file, ensure_ascii=False)

print(data)

print("Now downloading file(s) now..")
download_link = "https://your-nas-domain/webapi/DownloadStation/task.cgi?api=SYNO.DownloadStation.Task&version=1&method=create&uri=%s" % (link)

driver.get(download_link)
delay = 2

driver.get(download_task)
delay = 2
title = driver.find_element_by_tag_name("pre").text
data = json.loads(title)
with open('list.json', 'w', encoding='utf-8') as make_file:
    json.dump(title, make_file, ensure_ascii=False)
print(data)

download_file = "https://your-nas-domain/webapi/DownloadStation/task.cgi?api=SYNO.DownloadStation.Task&version=1&method=create&file=%s" % (file)
driver.get(download_file)
delay = 2

driver.get(download_task)
delay = 2
title = driver.find_element_by_tag_name("pre").text
data = json.loads(title)
with open('list.json', 'w', encoding='utf-8') as make_file:
    json.dump(title, make_file, ensure_ascii=False)
print(data)