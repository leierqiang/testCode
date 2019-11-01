data =[ ['a','b','c'],['a','b','c'],['a','b','c']]
with open("data_2.txt","w") as f:                                                   #设置文件对象
    for i in data:                                                                 #对于双层列表中的数据
        f.writelines(i)        