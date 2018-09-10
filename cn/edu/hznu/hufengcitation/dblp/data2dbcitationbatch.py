import logging
import time

from cn.edu.hznu import db

#insert paper into db
logger = logging.getLogger()
logger.setLevel(logging.INFO)
#rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
rq = time.strftime('%Y%m%d', time.localtime(time.time()))
log_name = 'D:\\py\\logs\\' + rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.INFO)  # 输出到file的log等级的开关

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# 定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

src_file="D:\\data\\DBLP\\DBLP_Citation_2014_May\\publications.txt"
f = open(src_file, mode='r',errors='ignore')
lines=[]
lines= f.readlines()
data_all =[]
linecount=0
totallines =  20797700
time_start=time.time()

year='0'
id='0'
ref=''

sql_str = 'insert into citation(citingid, citedid, citeyear) values(%s,%s,%s)'
values=[]
rec_count=1
for line in lines:
    linecount+=1
    #Data format
    # *Consistency in replicated continuous interactive media.
    # @Martin Mauve
    # t2000
    # cCSCW
    # index121834
    # %90514
    # %121960
    # %598576
    # %647871
    # %670879
    # %771899
    # %773619
    # %833085
    # %1117008
    # %1123640
    # !
    #process DBLP file
    if (line.startswith('#*')):
        year = '0'
        id = '0'
        ref = ''
    if (line.startswith('#t')):
        year = line.replace('#t','').replace('\n','').strip()
 #       year = int(line.replace('#t', ''))
    if (line.startswith('#index')):
        id = line.replace('#index','').replace('\n','').strip()
    if (line.startswith('#%')):
        ref = line.replace('#%','').replace('\n','').strip()
        if len(ref)>0:
            values.append((id, ref, year))
    if (line.startswith('#!')):
        rec_count += 1
        #        db.insert_one_rec(sql_str)
    if (rec_count % 200000==0)or(linecount==totallines):
        time_end = time.time()
        db.insert_batch_rec(sql_str, values)
        values = []
        logger.info('Inserted papers:%d, file lines: %d,%f%%, cost time:%d s',rec_count,linecount,linecount*1.0/totallines*100.0,time_end-time_start)
f.close()