import logging
import time
from collections import defaultdict

from pylab import *

from cn.edu.hznu import db

#insert paper into db
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#logger to file
#rq = time.strftime('%Y%m%d', time.localtime(time.time()))
#log_name = 'D:\\py\\logs\\' + rq + '_getrootfields.log'
#logfile = log_name
#fh = logging.FileHandler(logfile, mode='w')
#fh.setLevel(logging.INFO)  # 输出到file的log等级的开关
#logger.addHandler(fh)


# 定义handler的输出格式
#logger to console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
#fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(ch)
#logger.addHandler(fh)




#dir="f:\\data\\MAG-2016kdd\\MicrosoftAcademicGraph\\output\\"
src_dir="/home/zico/mag/output/"
dest_dir="/home/zico/mag/output/generate/"
#dir="D:\\data\\MAG\\output\\"
time_start=time.time()

src_file= src_dir + "papers_num.txt"
dest_file= dest_dir + "paper_growth_%s.txt"
#dest_citation_file= dir + "citing_%s_%s.txt"

sql_str_roots="select distinct rootid from fieldswithroot order by rootid ASC "
sql_str_subfield_of_one_root="select distinct id from fieldswithroot where rootid='%s' order by id ASC "
#sql_str_pubyear_of_all_papers="select id,pubyear from papers where id='%s' order by id ASC"
#sql_str_pubyear_of_all_papers_in="select id,pubyear from papers where id in (%s)  order by id ASC"
#sql_str_citations_of_all_papers="select paperid,refid from  paperreferences where refid='%s' order by paperid ASC"

#select b.id afrom paperkeywords a, papers b wehre i a.paperid=b.papers.id


totallines =  1417182
linecount=0
fieldYear={}
f = open(src_file,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
while line:
    linecount+=1
    #Data format
    #process MAG file
    if (linecount==1):
        line = f.readline()
        continue
    words=line.replace('\n','').split('\t')
    '''
    print(line)
    print(words[0])
    print(words[1])
    print(words[2])
    '''
    fileid=words[0]
    pubyear=int(words[1])
    citations = int(words[2])

    fieldYear.setdefault(fileid, {})[pubyear] = citations

    if (linecount % 500000==0)or(linecount==totallines):
#    if linecount>733400
        time_end = time.time()
        logger.info('Reading papers: %d,%f%%, cost time:%d s',linecount,linecount*1.0/totallines*100.0,time_end-time_start)
    line =f.readline()
f.close()


roots=[]
roots= db.get_query_results(sql_str_roots)
time_end=time.time()
logger.info('Done: Read Roots from DB! Time cost:%d s', time_end - time_start)

number_root_count=0
for root in roots:
    fields=[]
    number_root_count+=1
    str_root= "%s" % root
    tmp_sql_str_subfield_of_one_root= sql_str_subfield_of_one_root % str_root
    fields= db.get_query_results(tmp_sql_str_subfield_of_one_root)
    time_end=time.time()
    logger.info('Loading subfiled Done! Root:%s,#subfileds: %d,Time cost:%d s',str_root,len(fields),time_end - time_start)
    num_subfields_of_one_root = 0
    tmp_dest_file= dest_file % (str_root)
    root_year_papers_num=defaultdict(int)
    for field in fields:
        str_field= "%s" % field
        years=fieldYear.get(str_field)
        if years == None:
            continue
        for y in years:
            root_year_papers_num[y]+=fieldYear[str_field][y]
    papers=''
#    [(k, root_year_papers_num[k]) for k in sorted(root_year_papers_num.keys())]
    root_year_citation_num= sorted(root_year_citation_num,key=lambda x:x[0])
    for p in root_year_papers_num:
        papers = '%s%s\t%s\n' % (papers, p[0], p[1])
    dest_file_root = open(tmp_dest_file, encoding='UTF-8', mode='w', errors='ignore')
    dest_file_root.write(papers)
    dest_file_root.close()
    papers=None
    time_end = time.time()
    logger.info('Roots Generated. #subfields: %d, %d/%d:%f%%, time cost:%d', (len(fields)),
                number_root_count, len(roots), number_root_count * 1.0 / len(roots) * 100,    time_end - time_start)

