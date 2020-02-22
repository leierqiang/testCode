# coding:utf-8
# 采集豆瓣书信息和图片，写进数据库

from urllib import request
# from bs4 import BeautifulSoup
from lxml import etree
# import json, pymysql

# from my_pymysql import pymysql

url = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4"
headers = {
    'Host': 'book.douban.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}
req = request.Request(url=url, headers=headers, method="GET")
content = request.urlopen(req).read().decode("utf-8")
content_dict = etree.HTML(content)  # 格式化
# print(content_dict)
content_dict_allli = content_dict.xpath(r'//*[@id="subject_list"]/ul/li')  # 拿到列表
info_all = ''

for li in content_dict_allli:
    # 书名/标题
    title_list = li.xpath(r'div[2]/h2/a/@title')  # 取标签里的内容，注意地址是相对地址，不能直接拿来用 （注：和bs4不一样）
    title = title_list[0]
    title = title.replace(" ", '')
    print(title)
    # 信息 作者、出版社
    info_list = li.xpath(r'div[2]/div[1]/text()')
    author = info_list[0].split('/')[0]
    author = author.replace('\n', '').replace(" ", '')
    chubanshe = info_list[0].split('/')[1]
    print(author)
    print(chubanshe)
    # 评分
    pingfen_list = li.xpath(r'div[2]/div[2]/span[2]/text()')
    pingfen = pingfen_list[0]
    print(pingfen)

    # 图片
    img_net_addr = li.xpath(r'div[1]/a/img/@src')
    img_net_addr = img_net_addr[0]
    print(img_net_addr)
    data = request.urlopen(img_net_addr).read()
    img_name = str('douban/') + title + str('.jpg')
    with open(img_name, 'wb')as f:
        f.write(data)

    # # 数据库
    # db = pymysql.connect(host='localhost', port=3306, user="root", password='root', db='douban', charset='utf8')  #
    # cur = db.cursor()
    # sql = "insert into douban(title,author,chubanshe,pingfen)values('%s','%s','%s','%s')" % (
    # title, author, chubanshe, pingfen)
    # cur.execute(sql)
    # db.commit()
    # 
    # db.close()
