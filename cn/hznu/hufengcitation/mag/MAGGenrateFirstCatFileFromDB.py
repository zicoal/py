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

#dir="f:\\data\\MAG-2016kdd\\MicrosoftAcademicGraph\\"
dir="/home/zico/mag/"
time_start=time.time()

#dest_file= dir + "output_SubOfFirstField.txt"
#f_dest = open(dest_file, encoding='UTF-8', mode='w', errors='ignore')

sql_str_roots="select distinct parentid from fieldofstudyhierarchy where parentlevel='L0'"
sql_str_all_fields="select id, description from fieldsofstudies "
sql_get_all_subfild="select getChild('%s')"
sql_str = 'insert into fieldswithroot(id,thisdesc,rootid,rootdesc) values(%s,%s,%s,%s)'

roots=[]
roots= db.get_query_results(sql_str_roots)
time_end=time.time()
logger.info('Done: Read Roots from DB! Time cost:%d s', time_end - time_start)
#logger.info(roots[0])

all_fileds=[]
all_fileds= db.get_query_results(sql_str_all_fields)
time_end=time.time()
logger.info('Done: Read All Fields from DB! Time cost:%d s', time_end - time_start)
#logger.info(all_fileds[0])
linecount = 0
dict_fields_info= {}

for field in all_fileds:
    dict_fields_info.update({field[0]: field[1]})
#all discipines
#for root in roots:
#    print(dict_fields_info["%s" % root])
#exit()
for root in roots:
    sql_get_all_subfild_m = sql_get_all_subfild % root
    subfield = db.get_query_results(sql_get_all_subfild_m)
    linecount+=1
    time_end = time.time()
    logger.info('READ SUB FIELD OF ROOT %d,, time cost:%d s.', linecount,  time_end - time_start)
#   print(sql_get_all_subfild_m)
#    print(subfield)
#    print(len("%s" % subfield[0]))
    str_root="%s" % root
    root_field=dict_fields_info[str_root]
    str_root_subs=("%s" % subfield[0]).split(',')
    values=[]
    sub_dict_fields_info = {}
    for sub_field_id in str_root_subs:
        if sub_field_id.strip()!='#':
 #            if (len(sub_field_id)<8):
 #               logger.info("err sub field:%s",sub_field_id)
            if sub_dict_fields_info.get(sub_field_id) == None: #不重复插入子类数据
                sub_dict_fields_info.update({sub_field_id: "11"})
                values.append((sub_field_id,dict_fields_info[sub_field_id],str_root,root_field))
    sub_dict_fields_info ={}
    time_end = time.time()
    db.insert_batch_rec(sql_str, values)
    values = []
    logger.info('Inserted subs: %d,%f%%, cost time:%d s',linecount,linecount*1.0/len(roots)*100.0,time_end-time_start)