import requests
import lxml.etree as etree
import xml.etree.ElementTree as ET

# 详情页
# 3093-148
# http://www.etymon.cn/yingyucigen/148.html
def getTgePageDetails():
    for i in range(148, 153):
        url = "http://www.etymon.cn/yingyucigen/" + str(i) + ".html"
        data = {
            'Cookie': "__51cke__=; __tins__16789340=%7B%22sid%22%3A%201578926662444%2C%20%22vd%22%3A%2040%2C%20%22expires%22%3A%201578929234076%7D; __51laig__=40",
            'Referer': "http://www.etymon.cn/yingyucigen/list_1_37.html",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }

        res = requests.get(url, data=data, headers=headers)
        # print(res.content.decode("utf-8"))
        # 保存到文件中
        # with open("./词根.html", 'w', encoding="utf-8") as fp:
        #     fp.write(res.content.decode("utf-8"))

        # 解析
        html = etree.HTML(res.text)

        # 词根标题
        cigen_list = html.xpath('//*[@id="dictionary"]/dl/dt/h1')[0] #'//'表示获取当前节点子孙节点，'*'表示所有节点，'//*'表示获取当前节点下所有节点
        h1 = cigen_list.xpath('string(.)').strip()
        print(cigen_list)
        print(h1)
        # 保存
        with open("./cigen.html", 'a+', encoding="utf-8") as fp:
            print(i)
            fp.write(str(i))


        # # 正文
        # cigen_list = html.xpath('//*[@id="dictionary"]/dl/dd')[0]#'//'表示获取当前节点子孙节点，'*'表示所有节点，'//*'表示获取当前节点下所有节点
        # h1 = cigen_list.xpath('string(.)').strip()
        # print(cigen_list)
        # print(h1)
        # # 保存
        # with open("./cigen.html", 'a+', encoding="utf-8") as fp:
        #     print(i)
        #     fp.write(str(i))
        # #
        #
        #
        # # 保存
        # with open("./词根_处理完毕的.html", 'w', encoding="utf-8") as fp:
        #     fp.write(h1)

if __name__ == '__main__':
    getTgePageDetails()