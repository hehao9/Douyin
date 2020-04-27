import csv
import json
import re

temp_path = 'D:\\PycharmProjects\\Douyin\\user\\users.csv'


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
    if '/aweme/v1/user' in flow.request.url:  # 用户信息
        data = json.loads(flow.response.text)
        user = data.get('user')
        _user = {
            'USER_ID': user.get('uid'),
            'USER_DESCRIPTION': user.get('signature'),
            'SCHOOL': user.get('school_name'),
            'USER_NAME': user.get('nickname'),
            'USER_SEX': '女' if user.get('gender') == 2 else '男',
            'USER_BIRTHDAY': user.get('birthday'),
            'USER_IMAGE': user.get('avatar_thumb').get('url_list')[0],
            'USER_CITY': user.get('city'),
            'USER_INTEREST_NUM': user.get('following_count'),  # 关注数
            'USER_FANS': user.get('follower_count'),
            'BE_PRAISED_NUM': user.get('total_favorited'),  # 获赞数
            'WORKS_NUM': user.get('aweme_count'),
            'DYNAMIC': [],  # 近期发布过的视频
            'FAVORITE_WORKS': [], }
        append_csv([_user])
    elif '/aweme/v1/aweme/post' in flow.request.url:  # 最新视频
        user_list = read_csv()
        user_id = re.findall('user_id=(\d+)&', flow.request.url)[0]
        for user in user_list:
            if user['USER_ID'] == user_id:
                data = json.loads(flow.response.text)
                aweme_list = []
                if data.get('aweme_list'):
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
                        }
                        aweme_list.append(parse_para(aweme, para))
                user['DYNAMIC'] = aweme_list
                break
        write_csv(user_list)
    elif '/aweme/v1/aweme/favorite' in flow.request.url:  # 喜欢的作品
        user_list = read_csv()
        user_id = re.findall('user_id=(\d+)&', flow.request.url)[0]
        for user in user_list:
            if user['USER_ID'] == user_id:
                data = json.loads(flow.response.text)
                aweme_list = []
                if data.get('aweme_list'):
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
                        }
                        aweme_list.append(parse_para(aweme, para))
                user['FAVORITE_WORKS'] = aweme_list
                break
        write_csv(user_list)
