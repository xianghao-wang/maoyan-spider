import requests, re
import os

def get_one_page(url):
    """
        爬取具体一页 sample: url=https://maoyan.com/board/4?offset=0
        @param url: 要抓取页面的url
        @return: 网页的html
    """

    headers = {
        'User-Agent': os.getenv('USER_AGENT')
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return None
