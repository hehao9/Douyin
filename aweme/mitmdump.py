import json
import re
from mitmproxy import ctx

temp_path = 'D:\\PycharmProjects\\Douyin\\aweme\\aweme_list.json'


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
    if flow.request.url.startswith('https://aweme-hl.snssdk.com/aweme/v1/search/item'):
        data = json.loads(flow.response.text)
        aweme_list = []
        for aweme in data.get('aweme_list'):
            # aweme_list.append({
            #     'MUSIC': aweme.get('music').get('play_url').get('uri'),
            #     'DURATION': aweme.get('duration'),
            #     'TITLE': aweme.get('author').get('nickname'),  # 昵称
            #     'CONTENT': aweme.get('desc'),  # 描述
            #     'COMMENT_COUNT': aweme.get('statistics').get('comment_count'),
            #     'COMMENT_CONTANT': [],
            #     'REPEAT_COUNT': aweme.get('statistics').get('share_count'),
            #     'LIKE_NUM': aweme.get('statistics').get('digg_count'),
            #     'SAME_CITY': '',
            #     'FIRST_PAGE': '',
            #     'POST_USER_IMAGE': aweme.get('author').get('avatar_thumb').get('url_list')[0],
            #     'AUTHOR_USER_ID': aweme.get('author_user_id'),
            #     'AWEME_ID': aweme.get('aweme_id'), })
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
        with open(temp_path, 'w', encoding='utf-8') as file_obj:
            json.dump(aweme_list, file_obj, indent=4, ensure_ascii=False)
    elif flow.request.url.startswith('https://aweme-hl.snssdk.com/aweme/v2/comment/list'):
        with open(temp_path, encoding='utf-8') as file_obj:
            aweme_list = json.load(file_obj)
        aweme_id = re.findall('aweme_id=(\d+)&', flow.request.url)[0]
        for aweme in aweme_list:
            if aweme['AWEME_ID'] == aweme_id:
                data = json.loads(flow.response.text)
                comments = []
                for comment in data.get('comments'):
                    comments.append(comment.get('text'))
                aweme['COMMENT_CONTANT'] = comments
                break
        with open(temp_path, 'w', encoding='utf-8') as file_obj:
            json.dump(aweme_list, file_obj, indent=4, ensure_ascii=False)
