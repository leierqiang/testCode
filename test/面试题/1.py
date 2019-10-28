#!/usr/bin/env python
# encoding: utf-8

# 0.Python2、3内建数据类型有哪些，再分别标注可变类型和不可变类型
# Python3 6种：字符串String【不可变】、列表List【可变】、元组Tuple【不可变】、字典Dictionary【可变】、集合Set【可变】、数字Number(包括int、float)【不可变】
# Python2 5种：字符串String、列表List、元组Tuple、字典Dictionary、数字Number
# 注：集合和字典都是{}花括号

# 1.怎么在函数内部修改全局变量(注：不推荐实际中这么写)
a = 4
def func1():
    global a
    a = 5

if __name__ == '__main__':
    func1()
    print(a)
# 5


# 2.字典如何删除键和合并两个字典
dic1 = {'a':'aaa', 'b':'bbb'}
dic2 = {'c':'ccc', 'd':'ddd'}

# 删除
del dic1['a']
# 合并
dic1.update(dic2)

print(dic1)
# {'b': 'bbb', 'c': 'ccc', 'd': 'ddd'}

# 3.谈谈Python的CIL线程锁
# CPython解释器在设计的时候的遗留问题，线程在执行时会加一个CIL线程锁，得一个线城完毕后才能开始另一个线程
# 解决办法：用别的解释器(JPython等)或改用多进程(注：这个的资源消耗大)

# 4.列表怎么去重
list1 =  [1, 1, 2, 3, 3, 5]
set1 = set(list1)
list2 = [x for x in set1]
print(list2)
# [1, 2, 3, 5]

# 5.func(*args, **kwargs)意义与用法
# *args代表不定数量的非键值对的参数；**kwargs代表不定数量的可以是键值对的参数；一般两个是一起出现的
# 名称可以自己定，仅前面的* 、 ** 是固定的
def demo1(*args, **kwargs):
    print(args)
    for x in kwargs:
        print(x)

demo1('a','b', 'c', 'd', key1 = 'value1')
# ('a', 'b', 'c', 'd')
# key1

def demo2(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

demo2(key1 ='value1')
print('-------------')
demo2(key1 ='value1', key2 = 'value2')
# key1 value1
# ------------- #注：默认是一组键值对,当有两组时时执行两次(一般不会这么写)
# key1 value1
# key2 value2

# 6.Python2和3的区别
# 6.1  列表不一样range(10)，Python2返回列表、Python3种返回迭代器以节省内存

# Python2.X
# print range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Python3.X
print(range(10))
# range(0, 10)

# 6.2 print() 写法不一样,Python2可以不加(),Python3必须加
# 6.3 默认编码格式不一样，Python2是ascii，Python3是utf-8；因此Python2显示中文时必须引入coding声明
# 6.4 input() 函数不一样 Python2是raw_input() Python3是input()


# 7.举例说明map()函数的使用方法

# map(func(), 参数)   前面是方法，后面是参数，输出执行结果
def func(x):
    return x**2

list1 = [1, 2, 3, 4, 5]
if __name__ == '__main__':

    res = map(func, list1)
    print(res)
    print([i for i in res if i >10])

    # <map object at 0x000001C1588FB748>
    # [16, 25]

# 8.随机数
import random

print(random.random()) #注：1.random.random()不能传参 2.random.random 输出是一个对象
# 0.9731826298493651

# 9.数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句

# select distinct name from student


# 10.s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"

s = "ajldjlajfdljfddd"
s1= set(s)
l1 = [i for i in s1]
l2 = sorted(l1)
print(l2)
# ['a', 'd', 'f', 'j', 'l']

# 11.lambda函数的用法

res = lambda x:x**2
print(res(5))
# 25

# 12.字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"

# 注字母数字比较好去，中文字符不好去
import re

str1 = 'not 404 found 张三 99 深圳'
list1 = str1.split(' ')
res=re.findall('\d+|[a-zA-Z]+', str1)
for i in res:
    list1.remove(i)
print(list1)
# ['张三', '深圳']

# 13.合并两个列表，[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]

list1 = [1,5,7,9]
list2 = [2,2,6,8]

lis = list1+list2
print(sorted(lis))
# [1, 2, 2, 5, 6, 7, 8, 9]


# 14.统计图/数据可视化工具
# matplotlib 、帆软、Echarts

# 15.[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]

list1 = [[1,2],[3,4],[5,6]]
res = [j for i in list1 for j in i]
print(res)
# [1, 2, 3, 4, 5, 6]

# 16.zip()函数的使用方法
list1 = [1,2]
list2 = [3,4]

list3 = zip(list1, list2)
print(list(list3))

# 17.re/Python的正则模块 re.sub的用法

import re
a = "张明 98分"
res= re.sub(r'\d+', '100', a)
print(res)


# 18.数据库
# 优化方法:外键、索引、联合查询、选择特定字段
# 常用语句: show database;show table; desc 表名; select * from * where id =5;

# 19.提高Python运行效率的方法
# 使用生成器，节省内存
# 循环代码优化，避免过多重复代码的执行
# 核心模块用Cython PyPy等，提高效率
# 多进程、多线程、协程
# if else时候尽量把可能性最大的放在前面

# 20.遇到bug如何处理
# 1.关键位置print、同步做好开发日志
# 2.若是使用三方框架需要提前查阅官方文档或博客

# 20.简述cookie和session的区别
# cookie在客户端，session在服务端，因此cookie不安全
# session的id是存在cookie中的，如果禁用cookie session也会失效

# 21.IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
# IOError：输入输出异常
#
# AttributeError：试图访问一个对象没有的属性
#
# ImportError：无法引入模块或包，基本是路径问题
#
# IndentationError：语法错误，代码没有正确的对齐
#
# IndexError：下标索引超出序列边界
#
# KeyError:试图访问你字典里不存在的键
#
# SyntaxError:Python代码逻辑语法出错，不能执行
#
# NameError:使用一个还未赋予对象的变量

# 22.举例说明SQL注入和解决办法
# 当以字符串格式化书写方式的时候，如果用户输入的有;+SQL语句，后面的SQL语句会执行，比如例子中的SQL注入会删除数据库demo

# input_name = "name1"  #能组成正常sql、语句
# input_name = "name1;drap database demo"  #会造成sql注入
# sql = 'select * from demo where name ="%s"' % input_name
# # 解决办法：通过参数化方式解决
# input_name_list = [input_name]
# count = cs1.execute('select * from demo where name ="%s"' % input_name_list)

# 23.python垃圾回收机制
# python垃圾回收主要以引用计数为主，标记-清除和分代清除为辅的机制，其中标记-清除和分代回收主要是为了处理循环引用的难题;当有1个变量保存了对象的引用时，此对象的引用计数就会加1,当使用del删除变量指向的对象时，如果对象的引用计数不为1，比如3，那么此时只会让这个引用计数减1，即变为2，当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除

# 24.HTTP请求中get和post区别
# 1、GET请求是通过URL直接请求数据，数据信息可以在URL中直接看到，比如浏览器访问；而POST请求是放在请求头中的，我们是无法直接看到的；
# 2、GET提交有数据大小的限制，一般是不超过1024个字节，而这种说法也不完全准确，HTTP协议并没有设定URL字节长度的上限，而是浏览器做了些处理，所以长度依据浏览器的不同有所不同；POST请求在HTTP协议中也没有做说明，一般来说是没有设置限制的，但是实际上浏览器也有默认值。总体来说，少量的数据使用GET，大量的数据使用POST。
# 3、GET请求因为数据参数是暴露在URL中的，所以安全性比较低，比如密码是不能暴露的，就不能使用GET请求；POST请求中，请求参数信息是放在请求头的，所以安全性较高，可以使用。在实际中，涉及到登录操作的时候，尽量使用HTTPS请求，安全性更好。

# 25.python中读取Excel文件的方法
# pandas 的 read_excel方法

# 26.简述多线程、多进程

# 进程：
# 1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
#
# 2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制


# 线程：
# 1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，一个进程下的多个线程可以共享该进程的所有资源
# 2、如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃
#
# 应用：
# IO密集的用多线程，在用户输入，sleep 时候，可以切换到其他线程执行，减少等待的时间
# CPU密集的用多进程，因为假如IO操作少，用多线程的话，因为线程共享一个全局解释器锁，当前运行的线程会霸占GIL，其他线程没有GIL，就不能充分利用多核CPU的优势