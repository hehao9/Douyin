import csv
import re
import uuid

import requests
from tqdm import tqdm

temp_path = 'D:\\PycharmProjects\\Douyin\\aweme\\awemes.csv'


def read_csv():
    with open(temp_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
        dict_reader = csv.DictReader(csvfile)
        return [r for r in dict_reader]


def write_csv(rows):
    with open(temp_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        dict_writer = csv.DictWriter(csvfile, fieldnames=list(rows[0].keys()))
        dict_writer.writeheader()
        dict_writer.writerows(rows)


def downloadd(url, type):
    path = ''
    if len(url) > 0:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        }
        if type == 'music':
            path = f'D:/PycharmProjects/Douyin/source/{type}/{uuid.uuid4().hex}.mp3'
            r = requests.get(url, headers=headers)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
        if type == 'avatar':
            path = f'D:/PycharmProjects/Douyin/source/{type}/{uuid.uuid4().hex}.png'
            r = requests.get(url, headers=headers)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
        if type == 'video':
            path = f'D:/PycharmProjects/Douyin/source/{type}/{uuid.uuid4().hex}.mp4'
            r = requests.get(url, headers=headers)
            download_url = re.findall('playAddr: "(.*?)"', r.text)[0]
            r = requests.get(download_url, headers=headers)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
    return path


if __name__ == '__main__':
    aweme_list = read_csv()
    for aweme in tqdm(aweme_list):
        # 下载背景音乐
        aweme['MUSIC'] = downloadd(aweme.get('MUSIC'), 'music')
        # 下载作者头像
        aweme['POST_USER_IMAGE'] = downloadd(aweme.get('POST_USER_IMAGE'), 'avatar')
        # 下载短视频
        aweme['AWEME_URL'] = downloadd(aweme.get('AWEME_URL'), 'video')
    write_csv(aweme_list)
