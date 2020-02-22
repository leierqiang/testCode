# -*- coding: UTF-8 -*-

import urllib.request
from http import cookiejar
from http import cookies
from urllib import parse


#通过cookieJar类构建一个cookieJar对象，用来保存cookie的设置、

cookie=cookiejar.CookieJar()
#通过一个HttpCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
#参数就是构建的cookieJar对象、
cookie_handle=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(cookie_handle)
#人人网登陆接口
url='http://www.renren.com/PLogin.do'
data1={"email":"leierqiang@163.com","password":"qqq811562287"}

#通过urlencode()编码转换
data=urllib.parse.urlencode(data1).encode('utf-8')

request=urllib.request.Request(url,data=data)
response=opener.open(request)
print(response.read().decode('utf-8'))
