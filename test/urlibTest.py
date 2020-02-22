from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

cookjar = CookieJar()

handler = request.HTTPCookieProcessor(cookjar)
operner = request.build_opener(handler)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

data = {
    'email': "leierqiang@163.com",
    'password': "qqq811562287"
}

login_url = 'http://renren.com/PLogin.do'
req = request.Request(login_url, headers=headers, data=parse.urlencoede(data).encode('utf-8'))
# req = request.Request('http://httpbin.org/cookies', headers=headers)
request.urlopen(req)

dengluhou_url = "http://www.renren.com/880151247/profile"

req = request.Request(dengluhou_url, headers=headers)
resp = opener.open(dengluhou_url)
with open("renren.html", 'w', encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))

# resp = operner.open(req)
# print(resp.read())
#
# cookjar.save(ignore_discard=True, ignore_expires=True)
