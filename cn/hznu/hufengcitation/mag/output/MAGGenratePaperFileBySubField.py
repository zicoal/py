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
ch.setFormatter(formatter)
logger.addHandler(ch)
#logger.addHandler(fh)




#dir="f:\\data\\MAG-2016kdd\\MicrosoftAcademicGraph\\output\\"
dir="/home/zico/mag/output/allfields/paper/"
#dir="D:\\data\\MAG\\output\\"
time_start=time.time()

dest_file= dir + "paper_%s.txt"
#dest_citation_file= dir + "citing_%s_%s.txt"

sql_str_subfield="select distinct id from fieldswithroot order by id ASC "
sql_str_papers_of_all_subfields="select paperid,pubyear from paperkeywordswithyear where fieldid='%s' order by pubyear ASC "
#sql_str_pubyear_of_all_papers="select id,pubyear from papers where id='%s' order by id ASC"
#sql_str_pubyear_of_all_papers_in="select id,pubyear from papers where id in (%s)  order by id ASC"
#sql_str_citations_of_all_papers="select paperid,refid from  paperreferences where refid='%s' order by paperid ASC"

#select b.id afrom paperkeywords a, papers b wehre i a.paperid=b.papers.id


fields=[]
fields= db.get_query_results(sql_str_subfield)
time_end=time.time()
logger.info('Done: Read Roots from DB! Time cost:%d s', time_end - time_start)


num_subfields_of_all_roots = 0
#dict_fields_info= {}

#for root in roots:
#    print(dict_fields_info["%s" % root])
#exit()
for field in fields:
 #   dest_citation_file_root = dest_citation_file % (root[1],root[0])
    num_subfields_of_all_roots+=1
#    if num_subfields_of_one_root==1:
#        continue
    dest_file_field = dest_file % (field)
    f_dest = open(dest_file_field, encoding='UTF-8', mode='w', errors='ignore')
#    f_dest_citation = open(dest_citation_file_root, encoding='UTF-8', mode='w', errors='ignore')

    tmp_sql_str_papers_of_all_subfields = sql_str_papers_of_all_subfields % field
    all_papers = []
    all_papers = db.get_query_results(tmp_sql_str_papers_of_all_subfields)

    papers =''
    for p in all_papers:
        papers = '%s%s\t%s\n' % (papers, p[0], p[1])
    f_dest.write(papers)
    papers=None
    time_end = time.time()
    logger.info('Subfiled Generated. #subfields: %s, %d/%d:%f%%, #papers:%d, time cost:%d',  ("%s" % field), num_subfields_of_all_roots, len(fields), num_subfields_of_all_roots * 1.0 / len(fields) * 100, len(all_papers), time_end - time_start)
    f_dest.close()
#f_dest_citation.close()
