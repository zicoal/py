import logging
import time

from cn.edu.hznu import db

#insert paper into db
logger = logging.getLogger()
logger.setLevel(logging.INFO)
'''
#logger to file
#rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
#rq = time.strftime('%Y%m%d', time.localtime(time.time()))
#log_name = 'D:\\py\\logs\\' + rq + '.log'
#logfile = log_name
#fh = logging.FileHandler(logfile, mode='w')
#fh.setLevel(logging.INFO)  # 输出到file的log等级的开关
#fh.setFormatter(formatter)
#logger.addHandler(fh)
'''

# 定义handler的输出格式
#logger to console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
logger.addHandler(ch)

#dir="f:\\data\\MAG-2016kdd\\MicrosoftAcademicGraph\\"
dir="/home/zico/mag/"

src_file=dir+"PaperKeywords.txt"
err_file=dir+"PaperKeywords_error.txt"
f = open(src_file,encoding='UTF-8', mode='r',errors='ignore')
f_err = open(err_file,encoding='UTF-8', mode='w',errors='ignore')

lines=[]
lines= f.readlines()
data_all =[]
linecount=0
errcount=0
totallines =  158280968

time_start=time.time()

paperid='0'
fieldid=''
sql_str = 'insert into paperkeywords(paperid,fieldid) values(%s,%s)'
values=[]
rec_count=1
for line in lines:
    linecount+=1
    #Data format
    #process MAG file
    words=line.replace('\"','').replace('\n','').split('\t')
    paperid=words[0]
    fieldid=words[2]

    if(len(words)!=3):
        f_err.writelines(line)
        errcount+=1
        continue

    values.append((paperid, fieldid))

    if (linecount % 1000000==0)or(linecount==totallines):
        db.insert_batch_rec(sql_str, values)
        time_end = time.time()
        logger.info('Inserted papers: %d,%f%%, cost time:%d s',linecount,linecount*1.0/totallines*100.0,time_end-time_start)
        values = []
logger.error("error lines:%d.",errcount)
f.close()
f_err.close()