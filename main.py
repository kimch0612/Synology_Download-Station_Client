import urllib.request
import json

with open('account.json', 'rt', encoding='UTF8') as json_file:
    json_data = json.load(json_file)
    id = json_data["id"]
    pw = json_data["pw"]

urllib.request.urlretrieve("https://url/webapi/auth.cgi?api=SYNO.API.Auth&version=2&method=login&account=%s&passwd=%s&session=DownloadStation&format=cookie" % (id, pw), "login.json")
urllib.request.urlretrieve("https://url/webapi/DownloadStation/task.cgi?api=SYNO.DownloadStation.Task&version=1&method=list&format=cookie", "list.json")

with open('list.json', 'rt', encoding='UTF8') as json_file:
    json_data = json.load(json_file)
    dl_list = json_data["title"]

print(dl_list)