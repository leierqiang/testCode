import requests
import lxml.etree as etree
from bs4 import BeautifulSoup

# 拿到地址
def getTgePageDetails():
    # 3093 - 148
    for i in range(148, 160):
        url = "http://www.etymon.cn/yingyucigen/" + str(i) + ".html"
        parseThePage(url)

# 解析
def parseThePage(url):
    data = {
        'Cookie': "__51cke__=; __tins__16789340=%7B%22sid%22%3A%201578926662444%2C%20%22vd%22%3A%2040%2C%20%22expires%22%3A%201578929234076%7D; __51laig__=40",
        'Referer': "http://www.etymon.cn/yingyucigen/list_1_37.html",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }
    res = requests.get(url, headers=headers, data=data)
    htmlElement = etree.HTML(res.content)
    # res = etree.tostring(htmlElement, encoding="utf-8").decode('utf-8')  // 默认编码格式不清楚时候用这个强制转成utf-8
    # 词根标题
    cigen_title = htmlElement.xpath('//*[@id="dictionary"]/dl/dt/h1/text()')
    # 词根正文
    cigen_content = htmlElement.xpath('//*[@id="dictionary"]/dl/dd/text()')
    cigen_all =cigen_title[0] + "\r\n" + str([i for i in cigen_content])
    saveTheCigen(cigen_all)
    # print(cigen_all)

# 保存
def saveTheCigen(cigen_all):
    with open("./词根_处理完毕的.html", 'a+', encoding="utf-8") as fp:
        fp.write(cigen_all)

if __name__ == '__main__':
    getTgePageDetails()