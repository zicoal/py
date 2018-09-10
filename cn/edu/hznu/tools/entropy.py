import logging
import numpy as np

# 定义handler的输出格式
#logger to console
#logger_entropy = logging.getLogger()
#logger_entropy.setLevel(logging.INFO)
#ch1 = logging.StreamHandler()
#ch1.setLevel(logging.INFO)
#formatter1 = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
#ch1.setFormatter(formatter1)
#logger_entropy.addHandler(ch1)

#unnormalized
def get_entorpy(src):
#	>>> entorpy_sequence([1,1,2,1])
# 	>>> 0.811278
#	>>> entorpy_sequence([4,1,1,1])
#   >>0.811278

    l=len(src)
    value_list = set([src[i] for i in range(l)])
    ent = 0.0
    for x_value in value_list:
     #   logging.info("%d,%d",x_value  ,src.count(x_value))
        p = src.count(x_value)*1.0/l
        logp = np.log2(p)
        ent -= p * logp
    #print(len(value_list))
    if(len(value_list)==1):
        ent =0.0
#    else:
#        ent /= np.log2(len(value_list))
    return ent

def get_sequence_of_dict(src):
    s=[]
    return s

'''
s= [1,1,1,1]
print("result I: ", get_entorpy(s),)

s= [1,1,1,2]
print("result II: ", get_entorpy(s),)

s= [1,1,1,1,2]
print("result II': ", get_entorpy(s),)

s= [1,1,2]
print("result II'': ", get_entorpy(s),)

s= [1,2,2,2]
print("result III: ", get_entorpy(s))

s= [1,1,2,2]
print("result IV: ", get_entorpy(s))

s= [1,1,2,2]
print("result V: ", get_entorpy(s))

s= [1,2,2,3]
print("result VI: ", get_entorpy(s))

s= [1,2,3,3]
print("result VII: ", get_entorpy(s))

s= [1,1,2,3]
print("result VIII: ", get_entorpy(s))

s= [1,2,3,4]
print("result IX: ", get_entorpy(s))

s= [1,2,3,4,1]
print("result 8: ", get_entorpy(s))


s= [1,1,2,3]
print(get_entorpy(s))
'''
