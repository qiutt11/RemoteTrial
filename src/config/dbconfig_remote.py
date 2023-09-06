import pymysql



__author__ = '数据库连接'
def  pool_zdcd():
    db=pymysql.connect(host='10.100.19.113',user='test_hengyd',passwd='msdfHmm234*',db='jsd',port=3306,charset='utf8')
    return db