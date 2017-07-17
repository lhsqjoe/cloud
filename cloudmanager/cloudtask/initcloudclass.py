#!/usr/bin/python
import pymysql
connection = pymysql.connect(host='10.10.203.162', port=3306, user='root', passwd='vicloud.1', db='vcloud')

try:
    with connection.cursor() as cursor:
        sql='select * from T_USER'
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
    connection.commit()
finally:
    connection.close()


def alterTableStructure():
    print "alterTable"


def initTableData():
    print "init table data"

def initWebApp():
    print "init"
if __name__ == '__main__':
    #TODO 第一步修改数据库表
    alterTableStructure()
    #TODO 第二步导入数据
    initTableData()
    #TODO 清除
    initWebApp()
    #TODO 修改配置
    #TODO 重启tomcat6