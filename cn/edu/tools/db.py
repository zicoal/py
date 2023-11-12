#!/usr/bin/python
# coding:utf-8
import pymysql
import logging

def connect_db():
    return pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='mysqlphysics',
                           database='mag',
                           charset='utf8')


def insert_one_rec(sql_str):
    con = connect_db()
    cur = con.cursor()
    try:
        cur.execute(sql_str)
        con.commit()
    except:
        con.rollback()
        logging.exception('Insert operation error:' +sql_str)
        raise
    finally:
        cur.close()
        con.close()

def insert_batch_rec(sql_str,t_values):
    con = connect_db()
#    pymysql.connect(host='localhost', port=3306,
#                        user='username', passwd='password', db='database_name', charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = con.cursor()
    # SQL 插入语句 example
#   sql = "INSERT INTO EMPLOYEE(FIRST_NAME, AGE, SEX) VALUES (%s,%s,%s)"
    # 一个tuple或者list example
#    T = (('xiaoming', 31, 'boy'), ('hong', 22, 'girl'), ('wang', 90, 'man'))
    try:
        # 执行sql语句
        cursor.executemany(sql_str, t_values)
        # 提交到数据库执行
        con.commit()
    except:
        # 如果发生错误则回滚
        logging.exception('Insert operation error:' +sql_str)
        logging.exception(t_values)
        con.rollback()
        exit()
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    con.close()

#cols: The number of colums that should be obtained from DB
def get_query_results(sql_str):
    result = []
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute(sql_str)
        alldata = cur.fetchall()
        for rec in alldata:
            result.append(rec)
    except Exception as e:
        logging.error('SQL Error:'+sql_str)
    finally:
        cur.close()
        con.close()
    return result

#get the first query_result
def get_first_query_results(sql_str):
    result = []
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute(sql_str)
        alldata = cur.fetchall()
        return alldata[0]
    except Exception as e:
        logging.exception('Query Error:' + e+',SQL:'+sql_str)
    finally:
        cur.close()
        con.close()
    return result


#cols: The number of colums that should be obtained from DB
def get_query_results_add_enter(sql_str):
    result = []
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute(sql_str)
        alldata = cur.fetchall()
        for rec in alldata:
            result.append({rec,'\n'})
    except Exception as e:
        logging.exception('Query Error:' + e+',SQL:'+sql_str)
    finally:
        cur.close()
        con.close()
    return result