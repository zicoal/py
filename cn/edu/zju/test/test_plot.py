import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# 创建两个子图
fig, ax = plt.subplots(1, 1)

# 第一个子图
def getscore (x):
    b = 6
    c = 10
    return x**2 - b*x +c

x = [i/10 for i in range(10,50,1)]
y = [getscore(xi) for xi in x]
z = [xi for xi in x]

ax.plot(x,y,label="$f(x)=(x-3)^2+1$")
ax.plot(x,z,label="$f(x)=x$")
ax.set_xlabel('$x$',fontsize=15)
ax.set_ylabel('$f(x)$',fontsize=15)
ax.axvline(3,color="deeppink",linewidth=2,linestyle="--")
ax.legend(fontsize=10,loc="lower right", frameon=False)
# 第二个子图
#axs[1].scatter([1, 2, 3], [4, 5, 6])
#axs[1].set_title('Subplot 2')
#axs[1].legend(['Scatter'], loc='upper left', bbox_to_anchor=(0, 1))  # 显示图例

plt.show()