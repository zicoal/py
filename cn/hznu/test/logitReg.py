from numpy import *
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import statsmodels.api as sm
import pylab as pl
import copy

df = pd.read_csv("d:\py\\binary.csv")
#print dftrain.head()
#print df.describe()
df.columns = ["admit", "gre", "gpa", "prestige"]
#print df.columns
#print pd.crosstab(df['admit'], df['prestige'], rownames=['admit'])
#df.hist()
#pl.show()
dummy_ranks = pd.get_dummies(df['prestige'],prefix='prestige')
#print dummy_ranks.head()
cols_to_keep =  ['admit','gre','gpa']
data= df[cols_to_keep].join(dummy_ranks.ix[:,'prestige_2':])
#print data.head()
data['intercept'] = 1.0
#train
train_cols = data.columns[1:]
logit  = sm.Logit(data['admit'],data[train_cols])
result = logit.fit()
#test
combos = copy.deepcopy(data)
#print result
predict_cols = combos.columns[1:]
combos['intercept'] = 1.0
combos['predict']= result.predict(combos[predict_cols])
total=0
hit=0
for value in combos.values:
    predict = value[-1]
    admit = int(value[0])
    if predict > 0.5:
        total +=1
        if admit==1:
            hit+=1
print "Total: %d, Hit:%d, Precision:%.2f" % (total,hit,100.0*hit/total)
#print result.summary()
print combos.head()
colors = 'rbgyrbgy'
var = 'gre'
#pl.plot(combos[var], combos['predict'])
#for col in combos:
pl.scatter(combos[var], combos['predict'], marker = 'o')
pl.xlabel(var)
pl.ylabel("P(admit=1)")
pl.legend('o', loc='upper left', title='LogitRes')
pl.title("Prob(admit=1) isolating " + var + " and presitge")
pl.show()