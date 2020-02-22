# coding = "utf-8"

import requests
from urllib import request
from lxml import etree
import os
import re
from queue import Queue  # 队列
import threading


class Procuder(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Procuder, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        resp = requests.get(url, self.headers)
        text = resp.text
        html = etree.HTML(text)
        images_and_title = html.xpath('//div[@class="page-content text-center"]//img')  # 手写，不要复制粘贴xpath
        for img in images_and_title:
            img_url = img.get("data-original")
            img_name = img.get("alt")
            if img_url:
                suffix = os.path.splitext(img_url)[1]  # extension扩展 os.splitext是分割文件的扩展名
                filename = img_name + suffix
                filename = re.sub(r'[?？，!]*', '', filename)  # 有？等特殊字符就给去掉
                self.img_queue.put((img_url, filename))
                # print(filename)  # 有？等特殊字符就给去掉


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url, filename = self.img_queue.get()
            request.urlretrieve(img_url, 'images/' + filename)  # 下载图片
            print(filename + '  下载完成')


def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for i in range(1, 101):
        url = 'http://www.doutula.com/photo/list/?page=%d' % i
        # print(url)
        page_queue.put(url)

    for i in range(5):
        t = Procuder(page_queue, img_queue)
        t.start()

    for i in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()
