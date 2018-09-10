import logging
import time

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
#ch.setFormatter(formatter)
logger.addHandler(ch)
#logger.addHandler(fh)

dir="f:\\data\\MAG-2016kdd\\MicrosoftAcademicGraph\\output\\"
time_start=time.time()

dest_file= dir + "citation_%s_%s.txt"

sql_str_roots="select distinct rootid, rootdesc from fieldswithroot"
sql_str_subfield_of_one_root="select id from fieldswithroot where rootid='%s' order by id ASC "
sql_str_papers_of_all_subfields="select paperid from paperkeywords where fieldid='%s' order by paperid ASC "
sql_str_pubyear_of_all_papers="select paperid,refid from paperreferences where refid='%s' order by id ASC"
sql_str_citation_of_all_papers="select paperid,refid from paperreferences where refid='%s' order by id ASC"

#select b.id afrom paperkeywords a, papers b wehre i a.paperid=b.papers.id


roots=[]
roots= db.get_query_results(sql_str_roots)
time_end=time.time()
logger.info('Done: Read Roots from DB! Time cost:%d s', time_end - time_start)


rootcount = 0
dict_fields_info= {}

#for root in roots:
#    print(dict_fields_info["%s" % root])
#exit()
for root in roots:
    dest_file_root = dest_file % (root[1],root[0])
    rootcount+=1
    f_dest = open(dest_file_root, encoding='UTF-8', mode='w', errors='ignore')

    tmp_sql_str_subfield_of_one_root = sql_str_subfield_of_one_root % root[0]
    subfields_of_one_root=[]
    subfields_of_one_root= db.get_query_results(tmp_sql_str_subfield_of_one_root)
    time_end = time.time()
    num_subfields_of_one_root=0
    for subfield in subfields_of_one_root:
        tmp_sql_str_papers_of_all_subfields= sql_str_papers_of_all_subfields % subfield
 #       logger.info(tmp_sql_str_papers_of_all_subfields)
 #       exit()
        all_papers= []
        all_papers = db.get_query_results(tmp_sql_str_papers_of_all_subfields)
        time_end = time.time()
        logger.info('Get paperids.  root:%d, # of papers: %d time cost:%d', rootcount, len(all_papers),
                    time_end - time_start)
        papers =''
        for paper in all_papers:
             tmp_sql_str_pubyear_of_all_papers = sql_str_pubyear_of_all_papers % paper
             pubyear_of_all_papers = []
             pubyear_of_all_papers = db.get_query_results(tmp_sql_str_pubyear_of_all_papers)
             time_end = time.time()
#             logger.info('Get paper pubyears.  root:%d, # of paper pubyears: %d time cost:%d', rootcount, len(pubyear_of_all_papers),
#                         time_end - time_start)
             for p in pubyear_of_all_papers:
                 papers= papers+ ("%s\t%s\n" % (p[0],p[1]))
        f_dest.write(papers)
    num_subfields_of_one_root +=1
    time_end = time.time()
    logger.info('Paper Generated root:%d, # of subfields: %d/%d,%f%% time cost:%d',rootcount, num_subfields_of_one_root,len(subfields_of_one_root), num_subfields_of_one_root*1.0/len(subfields_of_one_root)*100,time_end - time_start)
    #logger.info('Paper Generated. root: %d,%f%%, cost time:%d s', rootcount,
    #                     rootcount * 1.0 / len(roots) * 100.0, time_end - time_start)
             #papers.append()
    f_dest.close()
