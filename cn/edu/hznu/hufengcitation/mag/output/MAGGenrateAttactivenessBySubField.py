import logging
import time
from collections import defaultdict

from pylab import *

from cn.edu.hznu.tools import db

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

src_paper_file= src_dir + "papers_fileds.txt"
src_paper_year_file= src_dir + "papers.txt"
src_citation_file= src_dir + "citations.txt"
dest_file= dest_dir + "attention_%s_%s.txt"

#dest_citation_file= dir + "citing_%s_%s.txt"

sql_str_roots="select distinct rootid from fieldswithroot order by rootid ASC "
sql_str_subfield_of_one_root="select distinct id from fieldswithroot where rootid='%s' order by id ASC "
#sql_str_pubyear_of_all_papers="select id,pubyear from papers where id='%s' order by id ASC"
#sql_str_pubyear_of_all_papers_in="select id,pubyear from papers where id in (%s)  order by id ASC"
#sql_str_citations_of_all_papers="select paperid,refid from  paperreferences where refid='%s' order by paperid ASC"

#select b.id afrom paperkeywords a, papers b wehre i a.paperid=b.papers.id




totallines_paper =  158280968
linecount=0
field_papers = {}
paper_year = {}
f = open(src_paper_file,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
while line:
    linecount+=1
    #Data format
    #process MAG file
    if (linecount==1):
        line = f.readline()
        continue
    words=line.replace('\n','').split('\t')

    fiedid=words[0]
    paperid=words[1]
    pubyear= int(words[2])

    field_papers.setdefault(fiedid, {})[paperid]=pubyear
    paper_year.setdefault(paperid, pubyear)
    #field_papers.setdefault(paperid, pubyear)
#    fields_paper_years.setdefault(fiedid, {})[paperid] =pubyear
    #[refid] = pubyear

    if (linecount % 1000000==0)or(linecount==totallines_paper):
#    if linecount>733400
        time_end = time.time()
        logger.info('Reading papers field years: %d,%f%%, cost time:%d s',linecount,linecount*1.0/totallines_paper*100.0,time_end-time_start)
    line =f.readline()
f.close()

totallines =  528682289
linecount=0
fieldCitations={}
f = open(src_citation_file,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
while line:
    linecount+=1
    #Data format
    #process MAG file
    if (linecount==1):
        line = f.readline()
        continue
    words=line.replace('\n','').split('\t')

    refid=words[0]
    fiedid=words[1]
    paperid=words[2]

    fieldCitations.setdefault(fiedid, {})[refid] =paperid

    if (linecount % 1000000==0)or(linecount==totallines):
#    if linecount>733400
        time_end = time.time()
        logger.info('Reading Citations: %d,%f%%, cost time:%d s',linecount,linecount*1.0/totallines*100.0,time_end-time_start)
    line =f.readline()
f.close()




roots=[]
roots= db.get_query_results(sql_str_roots)
time_end=time.time()
logger.info('Done: Read Roots from DB! Time cost:%d s', time_end - time_start)


t_0=1971
t_n=2010+1 # t_n+1
t_1=t_0+1
number_root_count=0

for root in roots:
    fields=[]
    number_root_count+=1
    str_root= "%s" % root
    tmp_sql_str_subfield_of_one_root= sql_str_subfield_of_one_root % str_root
    fields= db.get_query_results(tmp_sql_str_subfield_of_one_root)
    time_end=time.time()
    logger.info('Loading subfield Done! Root:%s,#subfileds: %d,Time cost:%d s',str_root,len(fields),time_end - time_start)
    num_subfields_of_one_root = 0
    tmp_dest_file= dest_file % (str_root, t_0)


    num_total_papers=0
    paper_t0_list={}
    root_year_citation_num = defaultdict(int)

    #find the initial papers
    for field in fields:
        str_field = "%s" % field
        paper_list = field_papers.get(str_field)
        if paper_list == None:
            continue
        for paper in paper_list:
            paper_id= "%s" % paper
            p=field_papers[str_field][paper_id] #paper_year.get(paper_id)
            if(p!=None  and p==t_0 ):
                paper_t0_list.setdefault(paper_id,p)
#                paper_t0_list.append(paper_id)

    logger.info('subfield Initial papers Loaded! Root:%s,#subfileds: %d, #Intial papers:%d, Time cost:%d s',str_root,len(fields),len(paper_t0_list),time_end - time_start)
    count_flag=0
    for field in fields:
        str_field= "%s" % field
        ref_list=fieldCitations.get(str_field)
        if ref_list == None:
            continue
        for ref in ref_list:
            ref_id= "%s" % ref
            paper_id="%s" % fieldCitations[str_field][ref]
            p_intial=paper_t0_list.get(ref_id) # is in the initial pubs?
            p_year=paper_year.get(paper_id) #
            if count_flag==0:
                logger.info("%s,%s,%s,%d",paper_id,ref_id,p_intial,p_year)
                count_flag=1
#            fieldCitations[str_field][paper]
            if(p_intial!=None and p_year!=None):
                root_year_citation_num[p_year]+=1
    citations=''
    root_year_citation_num= sorted(root_year_citation_num,key=lambda x:x[0])
#    [(k, root_year_citation_num[k]) for k in sorted(root_year_citation_num.keys())]
    for p in root_year_citation_num:
        citations = '%s%s\t%s\t%s\n' % (citations, p[0], p[1],len(paper_t0_list))
    dest_file_root = open(tmp_dest_file, encoding='UTF-8', mode='w', errors='ignore')
    dest_file_root.write(citations)
    dest_file_root.close()
    root_year_citation_num=None
    citations=None
    time_end = time.time()
    logger.info('One Root Generated. #subfields: %d, %d/%d:%f%%, time cost:%d', (len(fields)),
                number_root_count, len(roots), number_root_count * 1.0 / len(roots) * 100,    time_end - time_start)

