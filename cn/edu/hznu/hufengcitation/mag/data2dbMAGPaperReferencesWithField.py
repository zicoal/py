import logging
import time

from cn.edu.hznu.tools import db

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

src_file=dir+"PaperReferences.txt"
err_file=dir+"PaperReferences_error.txt"
src_paper_file=dir+"PaperKeywords.txt"
err_paper_file=dir+"PaperKeywords_error.txt"

f = open(src_file,encoding='UTF-8', mode='r',errors='ignore')
f_err = open(err_file,encoding='UTF-8', mode='w',errors='ignore')

f_paper_err = open(err_paper_file,encoding='UTF-8', mode='w',errors='ignore')
f_paper = open(src_paper_file,encoding='UTF-8', mode='r',errors='ignore')


lines=[]
#line= f.readline()
data_all =[]
linecount=0
errcount=0
totallines =  528682289
totallines_field =  158280968
time_start=time.time()

paperid='0'
refid=''
sql_str = 'insert into paperreferenceswithfield(paperid,refid,paperfieldid,reffieldid) values(%s,%s,%s,%s)'
values=[]
rec_count=1


paperField={}
line= f_paper.readline()
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


    paperField.update({paperid: fieldid})
    if (linecount % 1000000==0)or(linecount==totallines_field):
#    if linecount>733400
        time_end = time.time()
        logger.info('Read keywords: %d,%f%%, cost time:%d s',linecount,linecount*1.0/totallines_field*100.0,time_end-time_start)

    line=f_paper.readline()

f_paper.close()
f_paper_err.close()
linecount=0
line = f.readline()
while line:
    linecount+=1
    #Data format
    #process MAG file
    words=line.replace('\"','').replace('\n','').split('\t')
    paperid=words[0]
    refid=words[1]

    if(len(words)!=2):
        f_err.writelines(line)
        errcount+=1
        continue

    y=paperField.get(refid)
    if  y== None:
        y=''
    ff=paperField.get(paperid)
    if  ff== None:
        ff=''
    values.append((paperid, refid, ff,y))

    if (linecount % 1000000==0)or(linecount==totallines):
        db.insert_batch_rec(sql_str, values)
        time_end = time.time()
        logger.info('Inserted paperRefs: %d,%f%%, cost time:%d s',linecount,linecount*1.0/totallines*100.0,time_end-time_start)
        values = []
    line = f.readline()
logger.error("error lines:%d.",errcount)
f.close()
f_err.close()