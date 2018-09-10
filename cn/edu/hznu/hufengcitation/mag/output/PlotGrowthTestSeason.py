import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


dir="D:\\data\\MAG\\output\\paper_growth_citation_dist\\"

src_dir = dir+"generate\\paper_growth_%s.txt"


sns.set(color_codes=True)
np.random.seed(sum(map(ord, "regression")))

src_file = src_dir % "00F03FC7"

data = pd.read_csv(src_file,sep='\t',usecols=[0,1],names=['year','num'])
sns.lmplot(x="year", y="num", data=data)

#sns.jointplot(x="year", y="num", data=data,kind = 'kde')
#sns.pairplot(data)

plt.show()