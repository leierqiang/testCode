# from matplotlib import pylab as plt
# import random
#
# x = range(1, 121)
# y = [random.randint(20, 35) for i in range(120)]
# plt.plot(x, y)
# # 调整x轴刻度
# _x = list(x)[::10]
# _xtick_labels = ["hello{}".format(i) for i in _x]
# plt.xticks(_x[::2], _xtick_labels[::2], rotation=70)  # 间隔取值，再旋转70度
# plt.show()

"""
1.设置图片大小、分辨率
pylab.figure(figsize=(20,8),dpi=80)
2.保存到本地
plt.savefig("./sig_size.png")
3.加标题信息
pylab.title('5% Growth, Compunded Annually') #5%年复合增长率
pylab.xlabel('Years of Compounding') #年总数
pylab.ylabel('Value of Principal (“$”)') #本金价值/总钱数
4.调整xy轴刻度的间距、将int换成str格式内容
pylab.xticks(range(2,20,2))
---------------------------------------------------------
_x = list(x)[::10]
_xtick_labels = ["hello{}".format(i) for i in _x]
plt.xticks(_x[::2], _xtick_labels[::2], rotation=70) #间隔取值，再旋转70度
5.修改线条的样式
6.特殊点标记
7.加水印
"""

"""
实例：一笔10000元的投资，年回报率是5%，20年后能拿到多少钱？
"""
import pylab

principal = 10000
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate

pylab.plot(values)
pylab.title('5% Growth, Compunded Annually')  # 5%年复合增长率
pylab.xlabel('Years of Compounding')  # 年总数
pylab.ylabel('Value of Principal (“$”)')  # 本金价值/总钱数


pylab.xticks(range(1, 21, 2))
pylab.show()
