# coding = "utf-8"

import requests
from urllib import request
from lxml import etree
import os
import re


def main():
    baseurl = 'http://www.doutula.com/photo/list/?page={}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    for i in range(1, 2):
        resp = requests.get(baseurl.format(i), headers)
        text = resp.text
        html = etree.HTML(text)
        images_and_title = html.xpath('//div[@class="page-content text-center"]//img')  # 手写，不要复制粘贴xpath
        for img in images_and_title:
            img_url = img.get("data-original")
            img_name = img.get("alt")
            if img_url:
                suffix = os.path.splitext(img_url)[1]  # extension扩展 os.splitext是分割文件的扩展名
                filename = img_name + suffix
                filename = re.sub(r'[?？，!]', '', filename)  # 有？等特殊字符就给去掉
                print(filename)  # 有？等特殊字符就给去掉
                if not os.path.exists('images'):  # 如果没有目录就创建一个目录
                    os.mkdir('images')
                request.urlretrieve(img_url, 'images/' + filename) # 下载图片


if __name__ == '__main__':
    main()
