#!/usr/bin/python
# coding:utf-8


from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate


# 阴影误差图
# 参考https://blogs.mathworks.com/pick/2012/08/17/shaded-error-bars/
# 中间的实线是该类别的均值，上、下界是加上、减去n倍该类别的标准差。
def shaded_Error_Bar(category, values, n):
    values_down = [x.mean() - n * (np.array(x).std()) for x in values]  # 下界
    values_up = [x.mean() + n * (np.array(x).std()) for x in values]  # 上界
    values_mean = [x.mean() for x in values]  # 均值

    plt.plot(category, values_mean, 'red')
    plt.plot(category, values_down, 'pink')
    plt.plot(category, values_up, 'pink')

    plt.fill_between(category, values_down, values_up, color='red', alpha=0.25)

    plt.show()

def shaded_Error_Bar_Mean_Error(category, values_mean, errors, logx=False, n=1):
    values_up=[]
    values_down=[]
    num_count=0
    for x in values_mean:
        values_up.append(x + n * errors[num_count] )
        values_down.append(x - n * errors[num_count] )
        num_count+=1

    fig, axes = plt.subplots(1, 1, figsize=(5, 5))
    plt.plot(category, values_mean, linewidth=2, color='red')

    #fig
    plt.plot(category, values_down, 'pink')
    plt.plot(category, values_up, 'pink')

    if (logx == True):
        axes.set_xscale("log")

    plt.fill_between(category, values_down, values_up, color='red', alpha=0.25)


    plt.show()

#more parameters
#pars=[xlabel,ylabel, linewidth, color=[mean_color,bound_color],fig_file]
def shaded_Error_Bar_Mean_Error_Params(category, values_mean, errors, pars=[], logx=False,logy=False, n=1, isShow=True):
    values_up=[]
    values_down=[]
    num_count=0
    for x in values_mean:
        values_up.append(x + n * errors[num_count])
        values_down.append(x - n * errors[num_count] )
        num_count+=1

    colors=['red','pink']
    line_width=2
    fig_file=''
    xlabel=''
    ylabel=''

    fig, axes = plt.subplots(1, 1, figsize=(5, 5))

    if (pars[4] is not None):
        fig_file = pars[4]
    if (pars[3] is not None):
        colors = pars[3]
    if (pars[2] is not None):
        line_width = pars[2]
    if (pars[1] is not None):
        ylabel = pars[1]
        axes.set_ylabel(ylabel, size='15')
    if (pars[0] is not None):
        xlabel = pars[0]
        axes.set_xlabel(xlabel, size='11')

    plt.plot(category, values_mean, linewidth=line_width, color=colors[0])

    #fig
    plt.plot(category, values_down, colors[1])
    plt.plot(category, values_up, colors[1])

    if (logx == True):
        axes.set_xscale("log")
    if (logy == True):
        axes.set_yscale("log")

    plt.fill_between(category, values_down, values_up, color=colors[0], alpha=0.25)

    if(isShow==True):
        plt.show()
    else:
        plt.savefig(fig_file, dpi=400, bbox_inches='tight')

#more parameters
#pars=[xlabel,ylabel, linewidth, color=[mean_color,bound_color],fig_file]
def shaded_Error_Bar_Mean_Error_Params_SubPlot(category, values_mean, errors, subplot_pos, pars=[], logx=False,logy=False, n=1, isSave=False):
    values_up=[]
    values_down=[]
    num_count=0
    scale=0.3
    for x in values_mean:
        if (logy == True):
            values_up.append(x + n * errors[num_count])
            if(errors[num_count]/x>0.25):
                values_down.append((x - x*0.4))
            else:
                values_down.append((x - n * errors[num_count]))
        else:
            if (errors[num_count] / x > 0.25):
                values_up.append(x + x * scale)
                values_down.append((x - x * scale))
            else:
                values_up.append(x + n * errors[num_count])
                values_down.append((x - n * errors[num_count]))

        num_count+=1

    colors=['red','pink']
    line_width=2
    fig_file=''


    axes = plt.subplot(subplot_pos)

    if (pars[4] is not None):
        fig_file = pars[4]
    if (pars[3] is not None):
        colors = pars[3]
    if (pars[2] is not None):
        line_width = pars[2]
    if (pars[1] is not None):
        ylabel = pars[1]
        axes.set_ylabel(ylabel, size='10')
    if (pars[0] is not None):
        xlabel = pars[0]
        axes.set_xlabel(xlabel, size='7')

    plt.tick_params(labelsize=7)
    axes.plot(category, values_up, colors[1])
    axes.plot(category, values_down, colors[1])
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=None)
    plt.fill_between(category, values_down, values_up, color=colors[0], alpha=0.25)
    axes.plot(category, values_mean, linewidth=line_width, color=colors[0])

    if (pars[5] is not None):
        if (pars[6]==1):
            axes.text(2,95,pars[5])
        else:
            axes.text(1.5, 165, pars[5])

    if (logx == True):
        axes.set_xscale("log")
    if (logy == True):
        axes.set_yscale("log")


    if(isSave==True):
#        plt.savefig(fig_file, dpi=400, bbox_inches='tight')
        plt.savefig(fig_file, dpi=100, bbox_inches='tight')
        plt.cla()
        plt.clf()
        plt.close()


#more parameters
#pars=[xlabel,ylabel, linewidth, color=[mean_color,bound_color],fig_file]
def shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(category, values_mean, errors, subplot_pos, pars=[], logx=False,logy=False, n=1, isSave=False):
    values_up=[]
    values_down=[]
    num_count=0
    for x in values_mean:
        values_up.append(x + n * errors[num_count])
        values_down.append(x - n * errors[num_count] )
        num_count+=1

    colors=['red','pink']
    line_width=2
    fig_file=''
    xlabel=''
    ylabel=''

#    axes = plt.subplots(subplot_pos, figsize=(5, 5))

    axes = plt.subplot(subplot_pos)
#    if (pars[5] is not None):
 #      plt.legend("ddddddddddddddddd",loc='upper right')
    if (pars[4] is not None):
        fig_file = pars[4]
    if (pars[3] is not None):
        colors = pars[3]
    if (pars[2] is not None):
        line_width = pars[2]

    if (isSave==True):
        if (pars[1] is not None):
            ylabel = pars[1]
            ylabel_axis = pars[9]
#            axes.set_ylabel(ylabel, size='10')
            plt.text(ylabel_axis[0], ylabel_axis[1],  ylabel, rotation=90,
                  color='black', size='12', weight="light")
#            plt.text(ylabel_axis[0], ylabel_axis[1],  ylabel, rotation=90,
#                 family="fantasy", color='black', size='12', weight="light")

        if (pars[0] is not None):
            xlabel = pars[0]
            xlabel_axis = pars[8]
            plt.text(xlabel_axis[0], xlabel_axis[1], xlabel, \
                     color='black', size='12',  weight="bold")
#            plt.text(xlabel_axis[0], xlabel_axis[1], xlabel, \
#                     family="fantasy", color='black', size='12', weight="light")


    plt.tick_params(labelsize=7)
    #axes.plot(category, values_mean, linewidth=line_width, color=colors[0])
    #fig
    axes.plot(category, values_up, colors[1])
    axes.plot(category, values_down, colors[1])
    plt.fill_between(category, values_down, values_up, color=colors[0], alpha=0.25)

    axes.plot(category, values_mean, linewidth=line_width, color=colors[0])
#    plt.legend(pars[5], loc='upper right')
    if (pars[5] is not None):
#        axes.legend(pars[5],loc='upper right')
        pos=pars[7]-4  #the position

        if (pars[6]==1):

            xy=plt.axis()

            x= (xy[1] )/2
            y= (xy[3] )*0.9
            axes.text(x,y,pars[5], \
                    family = "fantasy", color = 'black', style = "italic", weight = "light")
#            axes.text(x,y,pars[5], \
#                    family = "fantasy", color = 'black', style = "italic", weight = "light")

        else:
            axes.text(0.9, 92, pars[5])


    if (logx == True):
        axes.set_xscale("log")
    if (logy == True):
        axes.set_yscale("log")

  #  print(subplot_pos)

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=None)

    if(isSave==True):

        plt.savefig(fig_file, dpi=100,  bbox_inches='tight')
#        plt.savefig(fig_file, dpi=1200,  bbox_inches='tight')
        plt.close('all')

#more parameters
#pars=[xlabel,ylabel, linewidth, color=[mean_color,bound_color],fig_file]
def shaded_Error_Bar_Mean_Error_Params_SubPlot_Smooth(category, values_mean, errors, subplot_pos, pars=[], logx=False,logy=False, n=1, isSave=False):
    values_up=[]
    values_down=[]
    num_count=0
    for x in values_mean:
        values_up.append(x + n * errors[num_count])
        values_down.append(x - n * errors[num_count] )
        num_count+=1

    colors=['red','pink']
    line_width=2
    fig_file=''
    xlabel=''
    ylabel=''

#    axes = plt.subplots(subplot_pos, figsize=(5, 5))

    axes = plt.subplot(subplot_pos)
#    if (pars[5] is not None):
 #      plt.legend("ddddddddddddddddd",loc='upper right')
    if (pars[4] is not None):
        fig_file = pars[4]
    if (pars[3] is not None):
        colors = pars[3]
    if (pars[2] is not None):
        line_width = pars[2]
    if (pars[1] is not None):
        ylabel = pars[1]
        axes.set_ylabel(ylabel, size='10')
    if (pars[0] is not None):
        xlabel = pars[0]
        axes.set_xlabel(xlabel, size='7')

    plt.tick_params(labelsize=7)
    #axes.plot(category, values_mean, linewidth=line_width, color=colors[0])
    #fig
    axes.plot(category, values_mean, linewidth=line_width, color=colors[0])
    if (pars[5] is not None):
#        axes.legend(pars[5],loc='upper right')
        if (pars[6]==1):
            axes.text(0.9,51,pars[5])
#            axes.text(0.9,51,pars[5], bbox = dict(facecolor = "r", alpha = 0.2))
        else:
            axes.text(0.9, 92, pars[5])

    #        axes.plot(category, values_mean, linewidth=line_width, color=colors[0],label=pars[5])
#        plt.legend(loc='upper right')

    if (logx == True):
        axes.set_xscale("log")
    if (logy == True):
        axes.set_yscale("log")

  #  print(subplot_pos)
    func1 = interpolate.interp1d(category, values_down, kind='cubic')
    xnew =np.arange(0,category[len(category)-1],0.00001)
    print(category)
    ynew_down = func1(xnew)
    axes.plot(xnew, ynew_down, colors[1])

    func2 = interpolate.interp1d(category, values_up, kind='cubic')
    ynew_up = func2(xnew)
    axes.plot(xnew, ynew_up, colors[1])

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=None)
    plt.fill_between(xnew, ynew_down, ynew_up, color=colors[0], alpha=0.25)

    if(isSave==True):
        plt.savefig(fig_file, dpi=1200, bbox_inches='tight')
'''
    plt.plot(x, y1, linewidth=2, color="#007500", label='log1.5(x)')
    plt.plot([1, 1], [y1[0], y1[-1]], "r--", linewidth=2)

    y2 = [math.log(a, 2) for a in x]
    plt.plot(x, y2, linewidth=2, color="#9F35FF", label="log2(x)")

    y3 = [math.log(a, 3) for a in x]
    plt.plot(x, y3, linewidth=2, color="#F75000", label="log3(x)"
                                                        - --------------------
    作者：半吊子Py全栈工程师
    来源：CSDN
    原文：https: // blog.csdn.net / qq_26877377 / article / details / 80200918
    版权声明：本文为博主原创文章，转载请附上博文链接！
'''