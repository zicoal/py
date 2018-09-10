#from matplotlib.pyplot import pause
from pandas import *
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'family': 'SimHei',
        'color':  'blue',
        'weight': 'normal',
        'size': 30,
        }
font2 = {'family': 'SimHei',
        'color':  'red',
        'weight': 'normal',
        'size': 30,
        }

src_file="D:\\manuscripts\\w王友贵的金融\\bank.txt"
dest_file="D:\\manuscripts\\w王友贵的金融\\bank_annual.txt"
f = open(src_file, encoding='UTF-8', mode='r',errors='ignore')
f_dest = open(dest_file, encoding='UTF-8', mode='w+')
lines=[]
data_all =[]
lines=f.readlines()
deposit_annual = []
loan_annual = []
for line in lines:
    words = line.replace("\n","").replace("\ufeff","").split("#")
#    deposit_annual.append([words[0],float(words[2])])
    deposit_annual.append([words[0],float(words[2])])
    loan_annual.append([words[0],float(words[3])])
#    data_all.append(words)
#    print(words)
f.close()
all_deposit_annual = DataFrame(deposit_annual)
all_loan_annual = DataFrame(loan_annual)
#print(all_deposit_annual)
#print(deposit_annual)
all_deposit_grouped = all_deposit_annual[1].groupby(all_deposit_annual[0])
all_loan_grouped = all_loan_annual[1].groupby(all_loan_annual[0])
#all_deposit_grouped = all_deposit_grouped.sum()
#print(all_deposit_grouped.mean())
#print(all_deposit_grouped.sum())
#common.draw_hist(all_deposit_grouped.sum()[1],20,'AreasList','Area','number',200112,201712,4000,8000000)
#print(all_deposit_annual)
#all_deposit_annual.
#    f_dest.write(line)
#f_dest.close()
all_deposit_grouped_show=all_deposit_grouped.sum()
all_loan_grouped_show=all_loan_grouped.sum()
#for line in all_deposit_grouped_show:
#    print((line))
#print(all_loan_grouped_show)
#print(all_deposit_grouped_show)
fig = plt.figure()
#ax = plt.gca()
#ax.yaxis.get_major_formatter().set_powerlimits((0,1))
ax1 = fig.add_subplot(111)
ax1.set_xlabel('时间')
ax1.set_ylabel('存/贷款款总额(亿元)')
ax1.set_title('国内银行存/贷款款趋势图')
plt.text(5,800000 , '---存款', fontdict=font1)
plt.text(5,700000 , '---贷款', fontdict=font2)
all_deposit_grouped_show.plot(kind='bar', color='blue')
all_loan_grouped_show.plot(kind='bar', color='red')
plt.show()



