# coding:utf-8
import requests
import time
import csv
from lxml import etree


def get_introduction_page_content(page):
    """
    在拉勾网首页搜“python”，地址选择“西安”，拿到目录页的内容
    :param page:当前页面的页数
    :return:返回CSV格式的数据
    """
    s = requests.session()
    Referer_list = "https://www.lagou.com/jobs/list_python?&px=default&city=%E8%A5%BF%E5%AE%89"
    url_xian_Python = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E8%A5%BF%E5%AE%89&needAddtionalResult=false"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Referer": Referer_list,
    }
    form_data = {
        "first": "true",
        "pn": page,
        "kd": "python"
    }

    # 获取“上一个页面”的cookie
    s.get(Referer_list, headers=headers, timeout=3)
    cookie = s.cookies

    response = s.post(url_xian_Python, data=form_data, headers=headers, cookies=cookie, timeout=3)
    response.raise_for_status()  # 如果请求失败就抛出异常
    response.encoding = response.apparent_encoding  # # 自动识别正文的编码格式 比 encoding、text 效果更好
    job_json = response.json()
    job_list = job_json['content']['positionResult']['result']
    csv_data = []
    for i in job_list:
        job_info = []
        job_info.append(i['positionId'])

        job_info.append(i['positionName'])  # 职位
        job_info.append(i['companyShortName'])  # 公司
        job_info.append(i['salary'])  # 薪资
        job_info.append(i['education'])  # 学历
        job_info.append(i['district'])  # 位置
        job_info.append(i['workYear'])  # 工作经验要求
        job_info.append(i['positionAdvantage'])  # 福利待遇
        csv_data.append(job_info)

        # 解析处理主页内容
        dowload_detial_page_content(i['positionId'])

    # 向csv文件里写入内容
    csvfile = open('python西安.csv', 'a+', encoding="utf-8", newline='')
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)
    csvfile.close()


def dowload_detial_page_content(id):
    """
    请求详情页的内容
    :param id:职位id
    :return:处理主页内容，待完善
    """
    detial_page_url = "https://www.lagou.com/jobs/%s.html" % (id)
    s = requests.session()
    Referer_list = "https://www.lagou.com/jobs/6771807.html?show=92a9ff5d3bdf4af5becd66fc3bb6f4e3"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Referer": Referer_list,
    }

    # 获取“上一个页面”的cookie
    s.get(detial_page_url, headers=headers, timeout=3)
    cookie = s.cookies
    response = s.post(detial_page_url, headers=headers, cookies=cookie, timeout=3)
    # 解析
    html = etree.HTML(response.text)
    position_miaoshu = html.xpath('//*[@id="job_detail"]/dd[2]/div/text()')
    # 保存
    with open("./职位详情.html", 'a+', encoding="utf-8") as fp:
        fp.write(str(position_miaoshu))


def main(numPage):
    # 新建一次csv文件的标题，后面的a+进去
    title = [('ID', '职位', '公司', '薪资', '学历', '位置', '工作经验要求', '福利待遇')]
    csvfile = open('python西安.csv', 'a+', encoding='utf-8', newline='')
    writer = csv.writer(csvfile)
    writer.writerows(title)
    csvfile.close()
    for page_num in range(1, numPage + 1):
        get_introduction_page_content(page_num)
        print('已抓取{}页'.format(page_num))
        time.sleep(15)  # 不能爬太快，容易被封(被封后直接在浏览器页看不到了)


if __name__ == '__main__':
    # 请求三页的
    main(3)
