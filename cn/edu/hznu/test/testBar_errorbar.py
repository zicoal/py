import matplotlib.pyplot as plt

x=[1,2,3,4,5]
#数据集
y=[20,44,21,64,46]
#误差列表
std_err=[1,2,5,3,2]

error_params=dict(elinewidth=4,ecolor='coral',capsize=5)#设置误差标记参数
#绘制柱状图，设置误差标记以及柱状图标签
plt.bar(x,y,color=['b','g','yellow','orange','gray'],yerr=std_err,error_kw=error_params,\
                    tick_label=['blue','green','yellow','orange','gray'])
#显示图形
plt.show()