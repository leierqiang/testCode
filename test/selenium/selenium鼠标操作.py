from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 引入 ActionChains 类

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')  


# 定位到要右击的元素
right_click = browser.find_element_by_link_text('新闻')

# 对定位到的元素执行鼠标右键操作
#ActionChains(driver)：调用ActionChains()类，并将浏览器驱动browser作为参数传入
#context_click(right_click)：模拟鼠标双击，需要传入指定元素定位作为参数
#perform()：执行ActionChains()中储存的所有操作，可以看做是执行之前一系列的操作
try:
    ActionChains(browser).context_click(right_click).perform()
    print('成功右击')
except Exception as e:
    print('fail')



