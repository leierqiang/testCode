from matplotlib import pylab as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simkai.ttf")
a = ["电影1", "电影2", "电影3", "电影4", ]
b = [56.01, 25.12, 45.21, 11.11]

# 设置图形大小
plt.figure(figsize=(20, 15), dpi=80)

# 绘制条形图
plt.bar(range(len(a)), b, width=0.3)
# 设置字符串到x轴
# plt.xticks(range(len(a)), a, fontpropertiex=my_font, rotation=90)
plt.xticks(range(len(a)), a, rotation=90)
plt.savefig("./move.png")
plt.show()


#
# import matplotlib
#
# print(matplotlib.matplotlib_fname())


# import matplotlib
# import matplotlib.pyplot as plt
# import random
#
# font = {'family': 'MicroSoft Yahei',
#         'weight': 'bold',
#         'size': 12}
# matplotlib.rc("font", **font)
#
# x = range(0, 120)
# y = [random.randint(20, 35) for i in range(120)]
# plt.figure(figsize=(20, 8), dpi=80)
# plt.plot(x, y)
#
# # 调整x轴刻度
# _x = list(x)[::3]
# _xtick_labels = ["10点{}分".format(i) for i in range(60)]
# _xtick_labels += ["11点{}分".format(i) for i in range(60)]
#
# # 取步长，数字和字符串一一对应，数据长度一样
# plt.xticks(_x, _xtick_labels[::3], rotation=45)  # rotation 旋转角度
# plt.show()