import re
import uuid

import requests

url = 'https://www.iesdouyin.com/share/video/6729703194672286980/?region=TW&mid=6729693420148804363&u_code=17l5j0dee&titleType=title'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
}
r = requests.get(url, headers=headers)
download_url = re.findall('playAddr: "(.*?)"', r.text)[0]
r = requests.get(download_url, headers=headers)
print(download_url)
with open(f'D:/PycharmProjects/Douyin/source/video/{uuid.uuid4().hex}.mp4', 'wb') as f:
    f.write(r.content)
    f.close()