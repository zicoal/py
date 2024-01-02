import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 生成数据
x = [1, 2, 3]
y = [4, 5, 6]
labels = ['A', 'B', 'C']
colors = ['red', 'green', 'blue']

# 绘制折线图
plt.plot(x, y)

# 添加图例
plt.legend()

# 设置图例标记为指定颜色
handles, labels = plt.gca().get_legend_handles_labels()
for handle in handles:
    handle.set_color('blue')

# 修改图例文本大小
fontsize = 10
plt.legend(prop={'size': fontsize})

# 显示图形
plt.show()