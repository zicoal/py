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
fig_file="D:\\我的坚果云\\ms\\h胡枫的引文网络\\JOI\\r1\\alpha-mle-dist-culmulative.png"

def formatnum(x):
    return '%.1f' % x

cul_aps=1
cul_dblp=1
with open(data_dist, 'r') as f:
	cul1=0
	cul2=0
	for i, line in enumerate(f):
		#print("%s, %s" %(i,line))
		m = line.replace('\n', '').split('\t')
		if(len(m[0] )>0):
			k1= int(m[0])
			dist1= float(m[1])
			cul_aps = cul_aps -cul1
			aps.setdefault(k1, cul_aps)
			cul1 = dist1
		if(len(m[2]) >0):
			k2= int(m[2])
			dist2= float(m[3])
			cul_dblp = cul_dblp -cul2
			dblp.setdefault(k2, cul_dblp)
			cul2 = dist2
#print(aps)
#print(dblp)
#sys.exit()
l=np.arange(0,2.01,0.05)
#print( data_alpha_dir % l[len(l)-1])
keys_aps=list(aps)
len_aps=len(keys_aps)
keys_dblp=list(dblp)
len_dblp=len(keys_dblp)
x=[]
y_aps=[]
y_dblp=[]
for filename in l:
	ff= data_alpha_dir % formatnum(filename)
	simulaiton = {}
	x.append(filename)
	with open(ff, 'r') as f:
		cul= 1
		cul1 = 0
		for i, line in enumerate(f):
			m = line.replace('\n', '').split('\t')
			if (len(m[0]) > 0):
				k1 = int(m[0])
				dist1 = float(m[1])
				cul = cul - cul1
				simulaiton.setdefault(k1, cul)
				cul1 = dist1
	mle=0
	length=0
	for key in keys_aps:
		if (simulaiton.get(key) is not None):
			mle += math.fabs(simulaiton.get(key)-aps.get(key))
			length+=1
	mle= mle/length
	y_aps.append(mle)

	mle=0
	length = 0
	for key in keys_dblp:
		if (simulaiton.get(key) is not None):
			mle += math.fabs(simulaiton.get(key)-dblp.get(key))
			length += 1
	mle= mle/length
	y_dblp.append(mle)

newticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
fig = plt.figure()
font={'weight':'black','size':15}

y1 = y_aps
y2 = y_dblp

ax2 = fig.add_subplot(111)
ax2.plot(x, y1,'D',c = 'skyblue',markersize=6, alpha=0.6,label='APS')
ax2.plot(x, y2,'o',c ='limegreen',markersize=6, alpha=0.6,label='DBLP')


#ax2.plot(newticks, y4,lw=4,c = 'grey',markersize=9, alpha=0.6,label='$y \sim e^{-0.75x^{0.75}}$ ')
#ax2.plot(xx, y5,lw=4,c = 'orange',markersize=9, alpha=0.6,label='$y \sim e^{-0.75x}$ ')
#ax2.plot(xx, y6,lw=4,c = 'orange',markersize=9, alpha=0.6,label='$y \sim e^{-0.85x}$ ')
#ax2.plot(newticks, y6,lw=4,c = 'r',markersize=9, alpha=0.6,label='$y \sim e^{-0.75x^{0.75}}$ ')
#ax2.plot(newticks, y4,lw=4,c = 'grey',markersize=9, alpha=0.6,label='$y \propto e^{-0.75x}$ ')

#
plt.legend(prop = font,shadow=True,loc="lower right")

# 字体设置
font_format = {'weight':'black', 'size':25}
plt.xlabel(r'$\alpha$',font_format)
font_format = {'weight':'bold', 'size':25}
plt.ylabel('MLE',font_format)

plt.xticks(fontproperties='oblique', size=10)
plt.yticks(fontproperties='oblique', size=10)
# 整个图像与展示框的相对位置
plt.subplots_adjust(left=0.15,right=0.95, bottom=0.15)
# 调整上下左右四个边框的线宽为2
ax=plt.gca()
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)

#

#plt.grid(axis="x",linestyle = '--')
plt.style.use( 'ggplot')
#plt.show()
#plt.savefig("Figure6.eps", dpi=600, format='eps', bbox_inches='tight')
plt.savefig(fig_file, dpi=200, bbox_inches='tight')

sys.exit()