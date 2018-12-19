# encoding=utf-8
from collections import defaultdict

# 字典的一键多值

print('方案一 list作为dict的值 值允许重复')

d1 = {}
key = 1
value = 2
d1.setdefault(key, []).append(value)
value = 3
d1.setdefault(key, []).append(value)

print (d1)

# 获取值
print ('方案一 获取值')
print (list(d1[key]))

for i in list(d1[key]):
    print(i)

print('方案一 删除值，会留下一个空列表')
d1[key].remove(2)
d1[key].remove(value)
print(d1)


print('方案一 检查是否还有一个值')
print(d1.get(key, []))

print('方案二 使用子字典作为dict的值 值不允许重复')

d1 = {}
key = 1
keyin = 1
value = 11
d1.setdefault(key, {})[keyin] = value
keyin = 2
value = 22
d1.setdefault(key, {})[keyin] = value
keyin = 3
value = 33
d1.setdefault(key, {})[keyin] = value

print(d1)

print('方案二 获取值')
print(list(d1[key]))
keys=d1[key]
keys=d1.get(key)
for k in keys:
    #1.setdefault(key, {})[k]  =  d1.setdefault(key, {})[k] +1
    d1[key][k] =d1[key][k]+1
    print(d1[key][k])

print('方案二 获取子健值')
print(d1[key][2])

print('方案二 删除值，会留下一个空列表')
del d1[key][keyin]
print(d1)
keyin = 2
del d1[key][keyin]
print(d1)

print('方案二 检查是否还有一个值')
print(d1.get(key, ()))

print('方案三 使用set作为dict的值 值不允许重复')
d1 = {}
key = 1
value = 2
d1.setdefault(key, set()).add(value)
value = 2
d1.setdefault(key, set()).add(value)
value = 3
d1.setdefault(key, set()).add(value)

print(d1)

print('方案三 获取值')
print
print(2 not in list(d1[key]))
print(2 in d1.get(key))

print('方案三 删除值，会留下一个空列表')
d1[key].remove(value)
value = 2
d1[key].remove(value)
print(d1)
print('方案三 检查是否还有一个值')
print
d1.get(key, ())

print('方案四 整数')
d=defaultdict(int)



key = 6
value = 2
key1 =1
value=1

key2 =2
value=3
print(d[key])
print(d[key2])
d[key1]+=1
d[key]+=2
d[key2]+=value
d[5]+=1
print(d[key])
print(d.get(key))
print(d[key2])
print(d.get(key2))

print(d.items())


print('---我是分割线------')
for p in d.items():
    print(p[0])
    print(p[1])
[(k,d[k]) for k in sorted(d.keys())]
print('---我是分割线------')
for p in d.items():
    print(p[0])
    print(p[1])

print('---我是分割线------')

a=2
b="ss"
c="%s %s" % (a,2.1)
print(c)

a={}
print(len(a))

print('方案物五 使用嵌套子字典作为dict的值 值不允许重复')

d1 = {}
key = 'Physics'
keyin1 = 'Chemistry'
keyin2 = 'Physics'
keyin11 = 2018
value1 = 10
value2 = 12
#d1.setdefault(key, {keyin1,{}})[keyin2] = value
d=d1.setdefault(key,{})
d2=d.setdefault(keyin1,{})
d2[keyin11]=value1
print(d1)
d.setdefault(keyin2,{})[keyin1] =value2

#d3=d.setdefault(keyin2,{})
#d3[keyin11]=value2

print(d1)