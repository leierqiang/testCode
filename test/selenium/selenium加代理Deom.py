# encoding:utf-8

from selenium import webdriver

chromedriver_path = "C:\Program Files\Anaconda\Scripts\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://182.108.63.184:9999")
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)

resp = driver.get("http://httpbin.org/ip")

