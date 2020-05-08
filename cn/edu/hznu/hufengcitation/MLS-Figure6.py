import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import sys
from matplotlib.ticker import MultipleLocator
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def fund(z, a, b):
	return z ** a + b

def fund_exp(z, a, b):
	return math.exp(a*z)  + b

x=[]
aps = []
dblp = []
exp = []
data_dist="D:\\我的坚果云\\ms\\h胡枫的引文网络\\JOI\\r1\\论文数据及图\\data-fig6.txt"
fig_file="D:\\我的坚果云\\ms\\h胡枫的引文网络\\JOI\\r1\\exp-fitting.png"

def formatnum(x):
    return '%.1f' % x

with open(data_dist, 'r') as f:
	for i, line in enumerate(f):
		#print("%s, %s" %(i,line))
		if i==0:
			continue
		m = line.replace('\n', '').split('\t')
		if(len(m[0] )>0):
			x.append(int(m[0]))
			aps.append(float(m[1]))
			dblp.append(float(m[2]))

#print( data_alpha_dir % l[len(l)-1])

newticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
fig = plt.figure()
font={'weight':'black','size':15}

ax2 = fig.add_subplot(121)

#xdata = np.linspace(0, 4, 50)
#print(type(xdata))
#print(type(x))
xdata=np.array(x)
ydata=np.array(dblp)
#y = fund(xdata, 0.75, 0.07)
ax2.plot(x, aps, 'b-')
popt, pcov = curve_fit(fund, xdata, ydata)
# popt数组中，三个值分别是待求参数a,b,c
y_exp1 = [fund(i, popt[0], popt[1]) for i in x]
y_exp2 = [fund_exp(i, -0.75, 0.04) for i in x]

ax2.plot(x, y_exp1, 'r--')
ax2.plot(x, y_exp2, 'g--')
print(y_exp2)
print("a:%s,b:%s" % (popt[0], popt[1]))



#print("min alpha(APS):%s,min:%s",min_alpha_aps,min_aps)
#print("min alpha(DBLP):%s,min:%s",min_alpha_dblp,min_dblp)

y1 = aps
y2 = dblp


#ax2.plot(x, y1,'D',c = 'skyblue',markersize=6, alpha=0.6,label='APS')
#ax2.plot(x, y2,'o',c ='limegreen',markersize=6, alpha=0.6,label='DBLP')

'''
#ax2.plot(newticks, y4,lw=4,c = 'grey',markersize=9, alpha=0.6,label='$y \sim e^{-0.75x^{0.75}}$ ')
#ax2.plot(xx, y5,lw=4,c = 'orange',markersize=9, alpha=0.6,label='$y \sim e^{-0.75x}$ ')
#ax2.plot(xx, y6,lw=4,c = 'orange',markersize=9, alpha=0.6,label='$y \sim e^{-0.85x}$ ')
#ax2.plot(newticks, y6,lw=4,c = 'r',markersize=9, alpha=0.6,label='$y \sim e^{-0.75x^{0.75}}$ ')
#ax2.plot(newticks, y4,lw=4,c = 'grey',markersize=9, alpha=0.6,label='$y \propto e^{-0.75x}$ ')

#
plt.legend(prop = font,shadow=False,loc="lower right")

# 字体设置
font_format = {'weight':'black', 'size':20}
plt.xlabel(r'$\alpha$',font_format)
font_format = {'weight':'bold', 'size':12}
plt.ylabel('Residual',font_format)

plt.xticks(fontproperties='oblique', size=8)
plt.yticks(fontproperties='oblique', size=8)
# 整个图像与展示框的相对位置
plt.subplots_adjust(left=0.15,right=0.95, bottom=0.15)
# 调整上下左右四个边框的线宽为2
ax=plt.gca()
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)

xy=plt.axis()
print(xy)
#plt.vlines(0.75, xy[2], xy[3], colors="pink", linestyles="dashed")
plt.axvline(x=0.75,color="pink", linestyle="dashed",lw=3)
plt.axvline(x=0.5,color="lightcoral", linestyle="dashed",lw=3)
#plt.grid(axis="x",linestyle = '--')
plt.style.use( 'ggplot')
#plt.show()
#plt.savefig("Figure6.eps", dpi=600, format='eps', bbox_inches='tight')
plt.savefig(fig_file, dpi=200, bbox_inches='tight')
'''
plt.savefig(fig_file, dpi=200, bbox_inches='tight')
sys.exit()