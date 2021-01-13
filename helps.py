import requests
import re
import os
import json

def get_one_page(url):
    """
        爬取具体一页 sample: url=https://maoyan.com/board/4?offset=0
        @param url: 要抓取页面的url
        @return: 网页的html文本
    """

    headers = {
        'User-Agent': os.getenv('USER_AGENT'),
        'Cookie': os.getenv('COOKIE')
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_one_page(html):
    """
        解析html文本
        @param html: 要被解析的html文本
        @return: generator[{
            'index', 'image', 'title', 'actor', 'time', 'score'
        }]
    """

    pattern = re.compile(r'<dd.*?board-index.*?>(.*?)</i>.*?<img.*?data-src="(.*?)".*?class="name".*?<a.*?>(.*?)</a>.*?star">(.*?)<.*?releasetime">(.*?)<.*?integer">(.*?)<.*?fraction">(.*?)<', re.S)
    items = re.findall(pattern, html)

    for item in items:
        yield{
            'index': item[0].strip(),
            'image': item[1].strip(),
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:0] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }

def write_to_file(content):
    with open(os.getenv('RESULT_FILE'), 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')