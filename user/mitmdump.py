import json
import re

temp_path = 'D:\\PycharmProjects\\Douyin\\user\\user.json'


def parse_para(data, para):
    ret = {}
    for k, v in para.items():
        if v:
            for vl in v:
                print(ret.get(k))
                x = ret[k].get(vl) if ret.get(k) else data.get(vl)
                if not x:
                    ret[k] = ''
                    break
                elif isinstance(x, list):
                    ret[k] = x[0]
                else:
                    ret[k] = x
        else:
            ret[k] = ''
    return ret


def response(flow):
    if flow.request.url.startswith('https://aweme-eagle-hl.snssdk.com/aweme/v1/user'):  # 用户信息
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
            'FAVORITE_WORKS': [],
            'FRIENDS_LIST': [], }
        with open(temp_path, 'w', encoding='utf-8') as file_obj:
            json.dump(_user, file_obj, indent=4, ensure_ascii=False)
    elif flow.request.url.startswith('https://api-hl.amemv.com/aweme/v1/aweme/post'):  # 最新视频
        with open(temp_path, encoding='utf-8') as file_obj:
            user = json.load(file_obj)
        user_id = re.findall('user_id=(\d+)&', flow.request.url)[0]
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
                        'SAME_CITY': [],
                        'FIRST_PAGE': [],
                        'POST_USER_IMAGE': ['author', 'avatar_thumb', 'url_list'],
                        'AUTHOR_USER_ID': ['author_user_id'],
                        'AWEME_ID': ['aweme_id'],
                    }
                    aweme_list.append(parse_para(aweme, para))
            user['DYNAMIC'] = aweme_list
        with open(temp_path, 'w', encoding='utf-8') as file_obj:
            json.dump(user, file_obj, indent=4, ensure_ascii=False)
    elif flow.request.url.startswith('https://api-hl.amemv.com/aweme/v1/aweme/favorite'):  # 喜欢的作品
        with open(temp_path, encoding='utf-8') as file_obj:
            user = json.load(file_obj)
        user_id = re.findall('user_id=(\d+)&', flow.request.url)[0]
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
                        'SAME_CITY': [],
                        'FIRST_PAGE': [],
                        'POST_USER_IMAGE': ['author', 'avatar_thumb', 'url_list'],
                        'AUTHOR_USER_ID': ['author_user_id'],
                        'AWEME_ID': ['aweme_id'],
                    }
                    aweme_list.append(parse_para(aweme, para))
            user['FAVORITE_WORKS'] = aweme_list
        with open(temp_path, 'w', encoding='utf-8') as file_obj:
            json.dump(user, file_obj, indent=4, ensure_ascii=False)
