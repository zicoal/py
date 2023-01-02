inputdata="""11317
4152
7160
3787
3247
3007
4642
4563
3669
5244
3904
10217
3580
8407
6981
17556
"""
sumtime = 0 #累积时间
n = 0 #序列索引
area = 0 #曲线下面积
x = [0]; y = [0] #累积时间
z = [0] #原始曲线
for line in inputdata.split():
    time = int(line)   
    sumtime += time
    area += (sumtime - 0.5 * time)#求面积
    n += 1
    x.append(n)#横轴
    y.append(sumtime)#纵轴
    z.append(time)#原始曲线

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
fig.set_size_inches(5, 5)
plt.plot(x, y, 'r-o', label = 'sumtime')#累积时间
plt.plot(x, z, 'g-x', label = 'time')#原始时间
plt.plot([0, n], [0, sumtime])#对角线
ax.text(n/2, sumtime, str(area / (sumtime * n)))#指标值
plt.legend()
plt.show()