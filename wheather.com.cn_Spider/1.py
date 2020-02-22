import re
import requests


def get_the_pagecountent(pageNum):
    base_url = 'https://www.gushiwen.org/default.aspx?page={}'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
    }

    res_all_list = []
    for i in range(pageNum):
        page_url = base_url.format(i)
        res_all = requests.get(page_url, headers=headers).text
        res_all_list.append(res_all)
    return res_all_list


def parse_the_page(res_all_list):
    for res_all in res_all_list:
        # shiciTitle = re.findall(r'style="font-size:18px; line-height:22px; height:22px;".*?<b>(.*?)</b>', res_all, re.DOTALL)  #	.匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
        shiciTitle = re.findall(r'style="font-size:18px; line-height:22px; height:22px;".*?<b>(.*?)</b>', res_all)
        print(shiciTitle)


if __name__ == '__main__':
    res_all_list = get_the_pagecountent(2)
    # print(res_all_list)
    parse_the_page(res_all_list)
