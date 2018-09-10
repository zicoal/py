src_file="D:\\data\\DBLP\\DBLP_Citation_2014_May\\publications.txt"
f = open(src_file, mode='r',errors='ignore')
lines=[]
lines= f.readlines()
data_all =[]
#banks=['工商银行','建设银行','中国银行','农业银行','交通银行']
linecount=0
for line in lines:
#    words = line.replace("\n","").replace("\ufeff","").split("#")
#    print(line)
    linecount = linecount+1
    if linecount == 10:
        exit()
f.close()