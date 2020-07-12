import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import sys
from matplotlib.ticker import MultipleLocator

aps = {}
dblp = {}
exp = []
data_alpha_dir="D:\\我的坚果云\\ms\\h胡枫的引文网络\\JOI\\r1\\data-alpha\\a=%s.txt"
data_dist="D:\\我的坚果云\\ms\\h胡枫的引文网络\\JOI\\r1\\data-fig4.txt"
fig_file="D:\\我的坚果云\\ms\\h胡枫的引文网络\\JOI\\r1\\Figure4-1"

fig_file_data="D:\\我的坚果云\\ms\\h胡枫的引文网络\\JOI\\r1\\论文数据及图\\fig4_data_all.txt"

def formatnum(x):
    return '%.1f' % x

with open(data_dist, 'r') as f:
	for i, line in enumerate(f):
		#print("%s, %s" %(i,line))
		if i==0:
			continue
		m = line.replace('\n', '').split('\t')
		if(len(m[0] )>0):
			k1= int(m[0])
			dist1= float(m[1])
			aps.setdefault(k1, dist1)
		if(len(m[2]) >0):
			k2= int(m[2])
			dist2= float(m[3])
			dblp.setdefault(k2, dist2)

#		print(aps)
#		print(dblp)
#		sys.exit()
l=np.arange(0,2.01,0.05)
#print( data_alpha_dir % l[len(l)-1])
keys_aps=list(aps)
len_aps=len(keys_aps)
keys_dblp=list(dblp)
len_dblp=len(keys_dblp)
x=[]
y_aps=[]
y_dblp=[]
min_alpha_aps=0
min_alpha_dblp=0
min_aps=1
min_dblp=1
for filename in l:
	ff= data_alpha_dir % formatnum(filename)
	simulaiton = {}
	x.append(filename)
	with open(ff, 'r') as f:
		for i, line in enumerate(f):
			m = line.replace('\n', '').split('\t')
			if (len(m[0]) > 0):
				k1 = int(m[0])
				dist1 = float(m[1])
				simulaiton.setdefault(k1, dist1)
	mle=0
	length=0
	for key in keys_aps:
		if (simulaiton.get(key) is not None):
			mle += math.fabs(simulaiton.get(key)-aps.get(key))
			length+=1
	mle= mle/length
	y_aps.append(mle)
	if(mle<min_aps):
		min_alpha_aps=filename
		min_aps=mle


	mle=0
	length = 0
	for key in keys_dblp:
		if (simulaiton.get(key) is not None):
			mle += math.fabs(simulaiton.get(key)-dblp.get(key))
			length += 1
	mle= mle/length
	y_dblp.append(mle)
	if(mle<min_dblp):
		min_alpha_dblp=filename
		min_dblp=mle

newticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
fig = plt.figure()
font={'weight':'black','size':12}

print("min alpha(APS):%s,min:%s",min_alpha_aps,min_aps)
print("min alpha(DBLP):%s,min:%s",min_alpha_dblp,min_dblp)

y1 = y_aps
y2 = y_dblp

ax2 = fig.add_subplot(211)
ax2.plot(x, y1,'D',c = 'skyblue',markersize=6, alpha=0.6,label='APS')
ax2.plot(x, y2,'o',c ='limegreen',markersize=6, alpha=0.6,label='DBLP')


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
plt.axvline(x=0.75,color="skyblue", linestyle="dashed",lw=3)
plt.axvline(x=0.5,color="limegreen", linestyle="dashed",lw=3)
plt.text(0.0,0.028,'(c)',fontsize=15, weight = "bold")

#plt.grid(axis="x",linestyle = '--')
plt.style.use( 'ggplot')
#plt.show()
#plt.savefig("Figure6.eps", dpi=600, format='eps', bbox_inches='tight')
plt.savefig(fig_file+".png", dpi=200, bbox_inches='tight')
plt.savefig(fig_file+".eps", dpi=600, format='eps', bbox_inches='tight')

sys.exit()