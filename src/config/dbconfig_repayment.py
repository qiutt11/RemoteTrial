#-*-coding:utf-8-*-
import pymysql

from DBUtils.PooledDB import PooledDB

__author__ = '数据库连接'
pool_zdcd1 = PooledDB(pymysql,5,host='10.100.19.113',user='test_hengyd',passwd='msdfHmm234*',db='test_hengyd',port=3306,charset='utf8')
