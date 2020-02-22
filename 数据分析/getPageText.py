from selenium import webdriver
from lxml import etree
from pyquery import PyQuery as pq
import time

driver = webdriver.Chrome() #实例化
driver.maximize_window()    #窗口最大化
driver.get('https://www.toutiao.com/')
driver.implicitly_wait(10)  #隐性等待10s【必须有，多加几个】
driver.find_element_by_link_text('科技').click()
driver.implicitly_wait(10)  #隐性等待10s
for i in range(3):
    js = "var q = document.documentElement.scrollTop="+str(i*500)
    driver.execute_script(js)
    time.sleep(2)

time.sleep(5)
page = driver.page_source
doc = pq(page)  #用pyquery实例化一下
doc = etree.HTML(str(doc))
contents = doc.xpath('//div[@class="wcommonFeed"]/ul/li')
print(contents) #这是一个对象
print("--------------------------")
for x in contents:
    title = x.xpath('div/div[1]/div/div[1]/a/text()')
    if title:
        title = title[0]
        # with open('toutiao.txt','a+',encoding='utf8')as f:
        #     f.write(title+'\n')
        print(title)
    else:
        pass

# 抓取今日头条——科技 内容title