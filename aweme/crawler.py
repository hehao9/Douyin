import csv
import json
import re
from mitmproxy import ctx

temp_path = 'D:\\PycharmProjects\\Douyin\\aweme\\awemes.csv'


def parse_para(data, para):
    ret = {}
    for k, v in para.items():
        if v:
            for vl in v:
                x = ret[k].get(vl) if ret.get(k) else data.get(vl)
                if isinstance(x, dict):
                    ret[k] = x
                elif isinstance(x, list):
                    ret[k] = x[0]
                else:
                    ret[k] = x
                    break
        else:
            ret[k] = ''
    return ret


def read_csv():
    with open(temp_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
        dict_reader = csv.DictReader(csvfile)
        return [r for r in dict_reader]


def write_csv(rows):
    with open(temp_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        dict_writer = csv.DictWriter(csvfile, fieldnames=list(rows[0].keys()))
        dict_writer.writeheader()
        dict_writer.writerows(rows)


def append_csv(rows):
    head = False if len(read_csv()) == 0 else True
    with open(temp_path, 'a', newline='', encoding='utf-8-sig') as csvfile:
        dict_writer = csv.DictWriter(csvfile, fieldnames=list(rows[0].keys()))
        if not head:
            dict_writer.writeheader()
        dict_writer.writerows(rows)


def response(flow):
    if '/aweme/v1/search/item' in flow.request.url:
        data = json.loads(flow.response.text)
        aweme_list = []
        for aweme in data.get('aweme_list'):
            para = {
                'MUSIC': ['music', 'play_url', 'uri'],
                'DURATION': ['duration'],
                'TITLE': ['author', 'nickname'],  # 昵称
                'CONTENT': ['desc'],  # 描述
                'COMMENT_COUNT': ['statistics', 'comment_count'],
                'COMMENT_CONTANT': [],
                'REPEAT_COUNT': ['statistics', 'share_count'],
                'LIKE_NUM': ['statistics', 'digg_count'],
                'POST_USER_IMAGE': ['author', 'avatar_thumb', 'url_list'],
                'AUTHOR_USER_ID': ['author_user_id'],
                'AWEME_ID': ['aweme_id'],
                'AWEME_URL': ['share_url'],
            }
            aweme_list.append(parse_para(aweme, para))
        append_csv(aweme_list)
    elif '/aweme/v2/comment/list' in flow.request.url:
        aweme_list = read_csv()
        aweme_id = re.findall('aweme_id=(\d+)&', flow.request.url)[0]
        for aweme in aweme_list:
            if aweme['AWEME_ID'] == aweme_id:
                data = json.loads(flow.response.text)
                comments = []
                if data.get('comments'):
                    for comment in data.get('comments'):
                        comments.append(comment.get('text'))
                aweme['COMMENT_CONTANT'] = comments
                break
        write_csv(aweme_list)
