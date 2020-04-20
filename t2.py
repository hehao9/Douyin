import json

temp_path = 'D:\\PycharmProjects\\Douyin\\aweme\\aweme_list.json'

with open(temp_path, 'w', encoding='utf-8') as file_obj:
    json.dump({'a': 11}, file_obj, indent=4, ensure_ascii=False)