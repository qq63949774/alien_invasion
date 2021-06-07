import matplotlib.pyplot as plt
from pylab import mpl
plt.style.use("ggplot") # 套用主题模板。
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()  # fig 表示整张图片。 变量ax表示图片中的各个图表。
ax.plot(input_values, squares, linewidth=3)
# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize = 24)
ax.set_xlabel("值", fontsize = 14)
ax.set_ylabel("值的平方", fontsize = 14)
# 设置刻度标记的大小。
ax.tick_params(axis ="both", labelsize = 14)
plt.show()