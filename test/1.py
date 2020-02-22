# coding:utf-8

class Parent(object):
    def __init__(self, name):
        print("parent的__init__开始被调用")
        self.name = name
        print("parent的__init__结束被调用")


class Son1(Parent):
    def __init__(self, name, age):
        print("Son1的__init__开始被调用")
        self.age = age
        # Parent.name = name
        Parent.__init__(self, name)
        print("Son1的__init__结束被调用")


class Son2(Parent):
    def __init__(self, name, gender):
        print("Son2的__init__开始被调用")
        self.gender = gender
        Parent.__init__(self, name)
        print("Son2的__init__结束被调用")


# class Grandson(Son1, Son2):
#     def __init__(self, name, age, gender):
#         print("Grandson的__init__开始被调用")
#         Son1.name = name
#         Son2.age = age
#         self.gender = gender
#         print("Grandson的__init__结束被调用")
#
#
# # Son1 = Son1("name1", 12)
# # print(Son1.name, Son1.age)
#
# Grandson = Grandson("name1", 12, "gender")
# print(Grandson.name, Grandson.age, Grandson.gender)
#
#
# # Grandson的__init__开始被调用
# # Grandson的__init__结束被调用
# # name1 12 gender


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print("Grandson的__init__开始被调用")
        Son1.__init__(self, name, age)
        Son2.__init__(self, name, gender)
        self.gender = gender
        print("Grandson的__init__结束被调用")


Grandson = Grandson("grandson", 12, "男")
print(Grandson.name, Grandson.age, Grandson.gender)

# Grandson的__init__开始被调用
# Son1的__init__开始被调用
# parent的__init__开始被调用
# parent的__init__结束被调用
# Son1的__init__结束被调用
# Son2的__init__开始被调用
# parent的__init__开始被调用
# parent的__init__结束被调用
# Son2的__init__结束被调用
# Grandson的__init__结束被调用
# grandson 12 男


"""
多重继承，注意调用顺序,理论上不应有方法多次执行、顺序不确定得执行

一个open()默认最多打开1024个文件
"""
