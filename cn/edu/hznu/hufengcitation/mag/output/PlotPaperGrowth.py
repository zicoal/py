import numpy as np
from pandas import *
from matplotlib import pyplot as plt
from pylab import *
import time
import logging
import os.path
import seaborn as sns
from IPython.core.pylabtools import figsize

#insert paper into db
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 定义handler的输出格式
#logger to console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
#fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(ch)
#logger.addHandler(fh)


dir="D:\\data\\MAG\\output\\"

src_file = dir+"paper_growth_citation_dist\\generate\\paper_growth_%s.txt"
root_file =dir +"RootInfo.txt"
fig_file = dir+"paper_growth_citation_dist\\graph\\paper_growth.png"
colors= ['black','bisque','lightgreen','slategrey','lightcoral','gold',
         'c','cornflowerblue','blueviolet','tomato','olivedrab',
         'lightsalmon','sage','lightskyblue','orchid','hotpink',
         'silver', 'slategray', 'indigo', 'darkgoldenrod','orange']


f = open(root_file,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
root_info=[]
time_start=time.time()

plt.rcParams['figure.figsize'] = (18, 10)

while line:
    #Data format
    #process MAG file
    words=line.replace('\n','').split('\t')

    rootid=words[0].strip()
    rootdesc=words[1].strip()

    root_info.append((rootid, rootdesc))

    line =f.readline()
f.close()

time_end = time.time()
logger.info('Read Roots Done, cost time:%d s', time_end - time_start)
num_root=0
root_info=sorted(root_info,key=lambda x:x[0])
for root in root_info:
    tmp_src_file=src_file % root[0]
#    logger.info(tmp_src_file)
    f = open(tmp_src_file,encoding='UTF-8', mode='r',errors='ignore')
    line =f.readline()
    x=[]
    y=[]
    while line:
        words = line.replace('\n', '').split('\t')

        year = words[0].strip()
        num = words[1].strip()
        y_s =int(year)

        if(y_s>=1950 and y_s < 2010):
            x.append(year)
            y.append(num)

        line = f.readline()
    plt.plot(x, y, linewidth='1', label=("%s" %  root[1]), color=colors[num_root], linestyle=':', marker='o')
    f.close()
    num_root+=1

#fig = plt.figure(1, (10, 6))
#plt.figure(figsize=(12,6))
ax = plt.gca()  # 获取当前图像的坐标轴信息
ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。


plt.legend(loc='upper left')
#plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0., handleheight=1.675)
plt.title('Temporal Growth Pattern',size ='30')
plt.xlabel('Year',size ='30')
plt.ylabel('# of Papers',size ='30')

#plt.gca().xaxis.set_major_locator(plt.NullLocator())
#plt.gca().yaxis.set_major_locator(plt.NullLocator())
#plt.subplots_adjust(top = 2, bottom = 2, right = 2, left = 20, hspace = 2, wspace = 2)
#plt.margins(0,0)

plt.savefig(fig_file,dpi=400,bbox_inches='tight')
#plt.draw()
#plt.show()
