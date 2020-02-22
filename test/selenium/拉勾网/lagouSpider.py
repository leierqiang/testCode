# coding:utf-8

import requests
from lxml import etree
import time


def request_list_page():
    s = requests.session()
    url = "https://www.lagou.com/jobs/list_python?city=%E8%A5%BF%E5%AE%89&cl=false&fromSearch=true&labelWords=&suginput="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Referer": "https://www.lagou.com/jobs/list_python/p-city_298?px=default",
        "Cookie": "_ga=GA1.2.825383708.1578658827; user_trace_token=20200110202030-9789aa88-33a3-11ea-b241-525400f775ce; LGUID=20200110202030-9789aed7-33a3-11ea-b241-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; LG_LOGIN_USER_ID=8d20f04034f635bf9ce06240cb8f5ef1ff1e35dac5bb4978; LG_HAS_LOGIN=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216f8f66c2288f6-08b07adf3b7fdb-2b7f2946-1329560-16f8f66c22933c%22%2C%22%24device_id%22%3A%2216f8f66c2288f6-08b07adf3b7fdb-2b7f2946-1329560-16f8f66c22933c%22%2C%22props%22%3A%7B%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2279.0.3945.117%22%7D%7D; _gid=GA1.2.1646889064.1580305660; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1578658827,1578807686,1578925517,1580305661; JSESSIONID=ABAAAECAAHHAAFD66FA838833BD4B35C92A87A2CB6C1183; LGSID=20200130132038-407edb68-4320-11ea-af21-5254005c3644; X_MIDDLE_TOKEN=9a70b4584659a4757c26d66d15127902; _gat=1; X_HTTP_TOKEN=58346b7a694a687f2365630851b362ba2f50946ee8; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1580365633; LGRID=20200130142712-8cf4110f-4329-11ea-8632-525400f775ce",
    }
    data = {
        "first": "false",
        "pn": "1",
        "kd": "python"
    }

    for i in range(1):
        data['pn'] = i
        s.get(url, headers=headers, timeout=3)
        # 如果返回的是字典，加json()会load成字典格式,如果不是字典这个方法会报错；可以在json.cn验证是否符合json格式
        cookie = s.cookies
        resp = requests.post(url, headers=headers, cookies=cookie, data=data,  timeout=3).json()
        time.sleep(2)
        print(resp)
        # positions = resp['content']['positionResult']['result']
        # for position in positions:
        #     positionId = position['positionId']
        #     positionurl = r"https://www.lagou.com/jobs/%s.html" % (positionId)
        #     # positionName = position['positionName']
        #     # companyFullName = position['companyFullName']
        #     # industryLables = position['industryLables']
        #
        #     print(position)
        # #     print("=" * 30)
        # #     return positionurl


def parse_position_detial(url):
    pass


def main():
    url = request_list_page()
    parse_position_detial(url)


if __name__ == '__main__':
    main()
