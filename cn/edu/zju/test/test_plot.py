import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# 创建两个子图
fig, axs = plt.subplots(1, 2)

# 第一个子图
axs[0].plot([1, 2, 3], [4, 5, 6])
axs[0].set_title('Subplot 1')
axs[0].legend(['Line'], loc='upper right', bbox_to_anchor=None)  # 显示图例

# 第二个子图
axs[1].scatter([1, 2, 3], [4, 5, 6])
axs[1].set_title('Subplot 2')
axs[1].legend(['Scatter'], loc='upper left', bbox_to_anchor=(0, 1))  # 显示图例

plt.show()