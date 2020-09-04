import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import sys
from matplotlib.ticker import MultipleLocator
from scipy import stats
from scipy.stats import ttest_rel
from scipy.stats import ks_2samp
from sklearn.metrics import roc_curve

fig_file="D:\\我的坚果云\\ms\\h胡枫的引文网络\\JOI\\r2\\Figure6."
fig_file_data="D:\\我的坚果云\\ms\\h胡枫的引文网络\\JOI\\r1\\论文数据及图\\fig6_data_all.txt"


APS = []
DBLP = []
Simulation = []
exp = []
with open('data.txt', 'r') as f:
	for i, line in enumerate(f):
		k = line.replace('\n', '')
		# 切片
		m=k.split('\t')
		APS.append(float(m[1]))
		DBLP.append(float(m[2]))
		Simulation.append(float(m[3]))
		exp.append(float(m[4]))


newticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
fig = plt.figure()
font={'weight':'black','size':15}
eta=-0.75
eta2=-0.6
x = np.arange(1,17)
y1 = APS
y2 = DBLP
y3 = Simulation
y4 = exp
y5=[]
y6=[]
newticks1 = np.arange(10,160)


count=0
y_aps=[]
y_dblp=[]
for i in newticks:
	if count==0:
		y_aps.append(1)
		y_dblp.append(1)
	else:
		y_aps.append(1.89*math.exp(eta*i)+0.07)
		y_dblp.append(1.5*math.exp(eta2*i)+0.05)
	count = 1

#print(y_dblp)
f=open(fig_file_data,'w')
f.writelines("APS\tAPS_Fit\tDBLP\tDBLP_Fit\n")
for i in range(len(APS)):
	f.writelines(str(APS[i])+"\t"+str(y_aps[i])+"\t"+str(DBLP[i])+"\t"+str(y_dblp[i])+"\n")
f.close()
#sys.exit()
t,p=ttest_rel(y1,y_aps)
#print(t,p)
t,p=ttest_rel(y2,y_dblp)
#print(t,p)
count=0
#xx=[i/10.0 for i in newticks1]
#print(xx)
for i in newticks1:
	if count==0:
		y5.append(1)
		y6.append(1)
	else:
		y5.append(1.89*math.exp(eta*i)+0.07)
		#y6.append(1.*math.exp(eta*i)+0.07)
		y6.append(1.6*math.exp(eta2*i)+0.05)
#		y5.append(math.exp(eta * i) )
#		y6.append(math.exp(eta2 * i) )
	count=1

#print(y1)
#print(y5)
#print("------------------------")
#print(y2)
#print(y6)
#print("len: %s %s" % (len(newticks),len(y_aps)))
ax2 = fig.add_subplot(121)
ax2.plot(newticks, y1,'D',c = 'skyblue',markersize=12, alpha=0.6,label='APS')
ax2.plot(newticks1, y5,lw=4,c = 'orange',markersize=9, alpha=0.6,label='$r \sim e^{-0.75t}$ ')
plt.legend(prop = font,shadow=True)

print(APS)
print(y_aps)

print(DBLP)
print(y_dblp)

b=[]
c=[]
sum1=sum(APS)
sum2=sum(y_aps)
for i in range(len(APS)):
    b.append(APS[i]/sum1)
    c.append(y_aps[i]/sum2)

print(sum1)
#a=ks_2samp(APS,y_aps)
a=ks_2samp(b,c)
print("APS KS: "  )
print(a )

sys.exit()
d=[]
e=[]
sum1=sum(DBLP)
sum2=sum(y_dblp)
for i in range(len(DBLP)):
    d.append(DBLP[i]/sum1)
    e.append(y_dblp[i]/sum2)

print(sum1)
f=ks_2samp(DBLP,y_dblp)
#f=ks_2samp(d,e)
print("DBLP KS: "  )
print(f  )
#print(b)
#print(c)
#print(d)
#print(e)

sys.exit()
#plt.text(6,0.2,'$p<10^{-8}$',fontsize=15)
plt.text(1,0.05,'(a)',fontsize=25)

# 字体设置
font_format = {'weight':'black', 'size':25}
plt.xlabel('t',font_format)
font_format = {'weight':'bold', 'size':25}
plt.ylabel('r',font_format)

plt.xticks(fontproperties='oblique', size=18)
plt.yticks(fontproperties='oblique', size=18)
# 整个图像与展示框的相对位置
# 调整上下左右四个边框的线宽为2
ax=plt.gca()
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)


ax2 = fig.add_subplot(122)
ax2.plot(newticks, y2,'o',c ='limegreen',markersize=15, alpha=0.6,label='DBLP')
ax2.plot(xx, y6,lw=4,c = 'orange',markersize=9, alpha=0.6,label='$r \sim e^{-0.5t}$ ')

#plt.text(6,0.2,'$p<10^{-9}$',fontsize=15)
plt.text(1,0.02,'(b)',fontsize=25)

#ax2.plot(newticks, y3,'s',c = 'pink',markersize=12, alpha=0.6,label='Simulation')


#ax2.plot(newticks, y4,lw=4,c = 'grey',markersize=9, alpha=0.6,label='$y \sim e^{-0.75x^{0.75}}$ ')
#ax2.plot(xx, y5,lw=4,c = 'orange',markersize=9, alpha=0.6,label='$y \sim e^{-0.75x}$ ')
#ax2.plot(xx, y6,lw=4,c = 'orange',markersize=9, alpha=0.6,label='$y \sim e^{-0.85x}$ ')
#ax2.plot(newticks, y6,lw=4,c = 'r',markersize=9, alpha=0.6,label='$y \sim e^{-0.75x^{0.75}}$ ')
#ax2.plot(newticks, y4,lw=4,c = 'grey',markersize=9, alpha=0.6,label='$y \propto e^{-0.75x}$ ')

#
plt.legend(prop = font,shadow=True)

# 字体设置
font_format = {'weight':'black', 'size':25}
plt.xlabel('t',font_format)


plt.xticks(fontproperties='oblique', size=18)
plt.yticks(fontproperties='oblique', size=18)
# 整个图像与展示框的相对位置
plt.subplots_adjust(left=0.5,right=1.95, bottom=0.15)
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
plt.savefig(fig_file+"eps", dpi=600, format='eps', bbox_inches='tight')
plt.savefig(fig_file+"png", dpi=200, bbox_inches='tight')
sys.exit()