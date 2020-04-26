import csv
import re


def read_csv():
    with open('test_dict_writer.csv', 'r', newline='', encoding='utf-8') as csvfile:
        dict_reader = csv.DictReader(csvfile)
        return [r for r in dict_reader]


def append_csv(rows):
    head = False if len(read_csv()) == 0 else True
    with open('test_dict_writer.csv', 'a', newline='', encoding='utf-8') as csvfile:
        dict_writer = csv.DictWriter(csvfile, fieldnames=list(rows[0].keys()))
        if not head:
            dict_writer.writeheader()
        dict_writer.writerows(rows)


# append_csv([{'firstname': 'Tom', 'lastname': ['Loya', '123']}])
url = 'https://aweme-eagle-hl.snssdk.com/aweme/v1/user'
print('snssdk.com/aweme/v1/user' in url)