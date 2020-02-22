import requests
from lxml import etree


def get_pic_url():
    base_url= "http://www.doutula.com/photo/list/?page={}"
    for i in range(1,3):
        page_url = base_url.format(i)
        resp = requests.get(page_url)

        # # res = requests.get(url, headers=headers, data=data)
        htmlElement = etree.HTML(resp.content)
        # print(htmlElement)
        # # res = etree.tostring(htmlElement, encoding="utf-8").decode('utf-8')  // 默认编码格式不清楚时候用这个强制转成utf-8
        # pic_url = htmlElement.xpath('//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[1]/img[@src]')
        pic_url = htmlElement.xpath('//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[1]/p/text()')
        print(type(pic_url[0]))
        for i in pic_url:
            print(type(i))
        # # print(str(pic_url[0]))

# get_pic_url()

def main():
    get_pic_url()

if __name__ == '__main__':
    main()