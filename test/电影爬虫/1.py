import requests
from lxml.html import etree

# 1.遍历页面拿到所有正文连接
def get_datial_urls():
    base_url = "https://dytt8.net/html/gndy/dyzz/list_23_{}.html"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }
    for i in range(1, 2):
        url = base_url.format(i)
        res_text = requests.get(url, headers = headers).content.decode("GBK") #强制用gbk解码，若报错就用先requests自己的库进行解码(res,text)，最后需要输出时再编码
        html =etree.HTML(res_text)
        detil_urls = html.xpath("//*[@id='header']//table[@class='tbspan']//a/@href")
        detil_urls = map(lambda url:"https://dytt8.net/" + url, detil_urls)  #匿名函数,返回一个匿名函数的对象，但是能遍历
        # for detil_url in detil_urls:
        #     print(detil_url)
        return detil_urls


# 2.解析页面
def parse_page(detil_url):
    pass

# 3.保存到文件
def save_to_txt(text):
    pass

def main():
    detil_urls = get_datial_urls()
    for detil_url in detil_urls:
        detial_all = parse_page(detil_url)
        save_to_txt(detial_all)

if __name__ == '__main__':
    main()