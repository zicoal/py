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
src_paper_file=dir+"Papers.txt"
err_paper_file=dir+"Papers_error.txt"
f = open(src_file,encoding='UTF-8', mode='r',errors='ignore')
f_paper = open(src_paper_file,encoding='UTF-8', mode='r',errors='ignore')
f_err = open(err_file,encoding='UTF-8', mode='w',errors='ignore')
f_paper_err = open(err_paper_file,encoding='UTF-8', mode='w',errors='ignore')

lines=[]
data_all =[]
linecount=0
errcount=0
totallines =  158280968
totallines_paper =  126909021

time_start=time.time()
paperYear={}
line= f_paper.readline()
while line:
    linecount+=1
    #Data format
    #process MAG file
    words=line.replace('\"','').split('\t')

    id=words[0]
    if len(words)<4:
        print(line)
        continue
    '''
    if(id=='7E900B06'):
      print(words)
      exit()
    '''
    if words[3].isdecimal():
        year =words[3]
    elif words[2].isdecimal():
        year=words[2]
    elif words[1].isdecimal():
        year = words[1]
    else:
        year = words[1][-4:]
    if(not year.isdecimal()):
        year = words[2][-4:]
    if((not year.isdecimal()) or (len(year) != 4)):
        f_paper_err.writelines(line)
        errcount+=1
        continue

    paperYear.update({id: year})

    if (linecount % 1000000==0)or(linecount==totallines_paper):
#    if linecount>733400
        time_end = time.time()
        logger.info('Read papers: %d,%f%%, cost time:%d s',linecount,linecount*1.0/totallines_paper*100.0,time_end-time_start)

    line=f_paper.readline()

f_paper.close()
f_paper_err.close()



paperid='0'
fieldid=''
sql_str = 'insert into paperkeywordswithyear(paperid,fieldid,pubyear) values(%s,%s,%s)'
values=[]
rec_count=1
line= f.readline()
linecount=0
while line:
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
    y=paperYear.get(paperid)
    if  y== None:
        values.append((paperid, fieldid,0))
    else:
        values.append((paperid, fieldid, y))

    if (linecount % 1000000==0)or(linecount==totallines):
        db.insert_batch_rec(sql_str, values)
        time_end = time.time()
        logger.info('Inserted paperkeywords: %d,%f%%, cost time:%d s',linecount,linecount*1.0/totallines*100.0,time_end-time_start)
        values = []
    line = f.readline()

logger.error("error lines:%d.",errcount)
f.close()
f_err.close()
