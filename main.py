import json
import sys
import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

with open('account.json', 'rt', encoding='UTF8') as json_file:
    json_data = json.load(json_file)
    nas = json_data["url"]
    id = json_data["id"]
    pw = json_data["pw"]

login_session = "https://%s/webapi/auth.cgi?api=SYNO.API.Auth&version=2&method=login&account=%s&passwd=%s&session=DownloadStation&format=cookie" % (nas, id, pw)
download_task = "https://%s/webapi/DownloadStation/task.cgi?api=SYNO.DownloadStation.Task&version=1&method=list&format=cookie" % (nas)

options = webdriver.ChromeOptions()
options.add_argument('log-level=2')
options.add_argument('window-size=1280x720')
options.add_argument('headless')
options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(login_session)
delay = 2
driver.implicitly_wait(delay)

def download_task_hamsu() :
    driver.get(download_task)
    delay = 2
    driver.implicitly_wait(delay)
    title = driver.find_element_by_tag_name("pre").text
    data = json.loads(title)
    with open('list.json', 'w', encoding='utf-8') as make_file:
        json.dump(title, make_file, ensure_ascii=False)
    print(data)

def download_link_hamsu() :
    link = input("다운로드 하고자 하는 URL을 입력해주세요 (파일 직링크 또는 마그넷 링크) : ")
    print("파일 다운로드 요청을 보내는 중..", end='')
    download_link = "https://%s/webapi/DownloadStation/task.cgi?api=SYNO.DownloadStation.Task&version=1&method=create&uri=%s" % (nas, link)
    driver.get(download_link)
    delay = 2
    driver.implicitly_wait(delay)
    print("완료!")

def download_file_hamsu() :
    file = input("토렌트 파일을 이곳에 드래그 하시거나 파일의 경로를 입력해주세요 : ")
    print("토렌트 파일을 업로드하는 중..", end='')
    download_file = "https://%s/webapi/DownloadStation/task.cgi?api=SYNO.DownloadStation.Task&version=1&method=create&file=%s" % (nas, file)
    driver.get(download_file)
    delay = 2
    driver.implicitly_wait(delay)
    print("완료!")

while True:
    whatyouwant = input("원하는 작업을 입력하세요 (현재 상태 / URL로 다운로드 / 파일로 다운로드 / 종료) : ")
    if whatyouwant == "현재 상태" or whatyouwant == "0":
        download_task_hamsu()
    elif whatyouwant == "URL로 다운로드" or whatyouwant == "1":
        download_link_hamsu()
    elif whatyouwant == "파일로 다운로드" or whatyouwant == "2":
        download_file_hamsu()
    elif whatyouwant == "종료" or whatyouwant == "3":
        driver.quit()
        sys.exit(1)
