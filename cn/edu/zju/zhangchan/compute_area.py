import matplotlib.pyplot as plt


'''
inputdata as a vector
'''
def getarea(inputdata):
    sumtime = 0  # 累积时间
    n = 0  # 序列索引
    area = 0  # 曲线下面积
    for line in inputdata:
        time = line
        sumtime += time
        area += (sumtime - 0.5 * time)  # 求面积
        n += 1

    return area / (sumtime * n)

def plot_getarea(inputdata):
    sumtime = 0 #累积时间
    n = 0 #序列索引
    area = 0 #曲线下面积
    x = []; y = [] #累积时间
    for line in inputdata.split():
        time = int(line)
        sumtime += time
        area += (sumtime - 0.5 * time)#求面积
        n += 1
        x.append(n)#横轴
        y.append(sumtime)#纵轴



#if __name__ == '__main__':
    fig, ax = plt.subplots()
    fig.set_size_inches(5, 5)
    plt.scatter(x, y)#序列图
    plt.plot([0, n], [0, sumtime])#对角线
    ax.text(0, sumtime, str(area / (sumtime * n)))#指标值
    #print(area / (sumtime * n))
    plt.show()

if __name__ == '__main__':

    inputdata="""
    7576
    1282
    996
    0
    0
    0
    0
    0
    0
    0
    0
    """
#    plot_getarea(inputdata)
    inputdata2 = [11342, 14219]
    print(getarea(inputdata2))
