# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:50:07 2016

@author: zico
"""
import matplotlib.pyplot as plt 
# matrix_A  训练集  
matrix_A = [[1,1,4], [1,2,5], [1,5,1], [1,4,2]]
Matrix_y = [19,26,18]
theta = [3,2,4]
#学习速率  
leraing_rate = 0.005  
loss = 50  
iters = 1  
Eps = 0.0001  
while loss>Eps:
    loss = 0  
    for i in range(3) :  
        h = theta[0]*matrix_A[i][0] + theta[1]*matrix_A[i][1] + theta[2]*matrix_A[i][2]
        theta[0] = theta[0] - leraing_rate*(h-Matrix_y[i])*matrix_A[i][0]
        theta[1] = theta[1] - leraing_rate*(h-Matrix_y[i])*matrix_A[i][1]
        theta[2] = theta[2] - leraing_rate * (h - Matrix_y[i]) * matrix_A[i][2]
    for i in range(3) :
        Error = 0  
        Error = theta[0]*matrix_A[i][0] + theta[1]*matrix_A[i][1]  + theta[2]*matrix_A[i][2] - Matrix_y[i]
        Error = Error * Error
        loss = loss +Error  
#        print ('Error=', Error,loss )
    iters = iters +1
    #print ('loss=', loss)
#for i in range(3) :  
#    plt.plot(matrix_A[i][1], theta[1]*matrix_A[i][1],'r--', linewidth=2)
#    print matrix_A[i][1]
plt.plot(theta,Matrix_y,'r--')
#plt.xlim(0, 6)
#plt.ylim(0, 17)
plt.xlabel("areas")
plt.ylabel("price")
#plt.legend()
plt.show()
print ('theta=',theta)  
print ('iters=',iters)