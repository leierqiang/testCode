# 保存 cookie 到变量
import urllib.request
import http.cookiejar

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://flights.ctrip.com/')

for item in cookie:
    print('%s = %s' % (item.name, item.value))

# 保存 cookie 到文件
import urllib.request
import http.cookiejar

# cookie_file = 'E:/mypy/cookie.txt'
cookie_file = './cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(cookie_file)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
# response = opener.open('http://flights.ctrip.com/')
request = urllib.request.Request('http://flights.ctrip.com/', headers={"Connection": "keep-alive"})
response = opener.open(request)
cookie.save(ignore_discard=True, ignore_expires=True)

for item in cookie:
    print('%s = %s' % (item.name, item.value))

# 从文件中读取 cookie 访问
import urllib.request
import http.cookiejar

# cookie_file = 'E:/mypy/cookie.txt'
cookie_file = './cookie.txt'
cookie = http.cookiejar.MozillaCookieJar()
cookie.load(cookie_file, ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
request = urllib.request.Request('http://flights.ctrip.com/')
html = opener.open(request).read().decode('gbk')
print(html)