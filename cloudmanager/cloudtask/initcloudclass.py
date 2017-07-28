#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql
import paramiko

projectName = 'cloud-manager'
tomcatDir = '/var/lib/tomcat6/webapps'
hostIp = ''
osUser = 'root'
osPwd = ''
distPath = '/opt/setup/'
configFilePath = '/opt/config.note'
sshPort = 22

# DataBase
dbIp = ''
dbName = 'vcloud'
dbUser = 'root'
dbPwd = ''
# rabbitMQ
mqIp = ''
mqPort = '5672'
mqUser = 'guest'
mqPwd = 'eucalyptus'



def init_data():
    global hostIp, dbIp, mqIp,dbPwd,osPwd
    f = open(configFilePath)
    lines = f.readlines()  # 读取全部内容
    for line in lines:
        arrayOne = line.replace("\n", "").split(':')
        if 'IP Addr' in arrayOne[0]:
            hostIp = arrayOne[1].strip()
            dbIp = arrayOne[1].strip()
            mqIp = arrayOne[1].strip()

        if 'DATABASE PASSWD' in arrayOne[0]:
            dbPwd = arrayOne[1].strip()
        if 'ROOT PASSWD' in arrayOne[0]:
            osPwd = arrayOne[1].strip()
    # print 'hostip:' + hostIp + ' dbIP:' + dbIp + ' mqIp:' + mqIp + ' dbPwd:' + dbPwd + ' osPwd:' + osPwd


def exceCmd(cmdList,host=hostIp,userName=osUser,pwd=osPwd,port=sshPort):
    paramiko.util.log_to_file('syslogin.log')
    trans = paramiko.Transport((host,port))
    trans.connect(username=userName, password=pwd)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh._transport = trans
    resList = []
    for cmdStr in cmdList:
        print cmdStr
        stdin, stdout, stderr = ssh.exec_command(cmdStr)
        resStr = stdout.read().decode()
        print(resStr)
        resList.append(resStr)
    trans.close()
    return resList


def alterTableStructure():
    conn = pymysql.connect(host=hostIp, port=3306, user=dbUser, passwd=dbPwd, db=dbName)
    try:
        with conn.cursor() as cursor:
            cursor.execute("TRUNCATE T_MENU")
            cursor.execute("TRUNCATE T_ROLE_PERMISSION")
            cursor.execute("TRUNCATE T_ROLE")
            cursor.execute("TRUNCATE T_USER_ROLE")
            cursor.execute("ALTER TABLE T_BOX ADD (CPUINFO VARCHAR(20) ,MEMERYINFO VARCHAR(20),USBSTATE VARCHAR(20))")
            cursor.execute("ALTER TABLE T_NC ADD (CREATE_TIME TIMESTAMP ,STATE VARCHAR(20))")
            cursor.execute("ALTER TABLE T_COURSES ADD (COURSES_SIZE FLOAT ,COURSES_PATH VARCHAR(255),COURSES_DEFAULT INT(1))")
            cursor.execute("ALTER TABLE T_INSTANCE ADD (DESKTOP_NUM VARCHAR(40),COURSES_NAME VARCHAR(50))")
            cursor.execute("ALTER TABLE T_INSTANCE engine=innodb")
            conn.commit()
    except Exception:
        print 'alter database fail'
    finally:
        conn.close()


def initTableData():
    sql = 'mysql -h '+hostIp+' -u root -p"' + dbPwd + '"  ' + dbName + ' < ' + distPath + 'vcloud.sql'
    exceCmd([sql], hostIp, osUser, osPwd, sshPort)


def initWebApp():
    exceCmd(['unzip -oq ' + distPath  + projectName + '.war' + ' -d ' + distPath + projectName],hostIp,osUser,osPwd,sshPort)
    configPath = distPath + projectName + '/WEB-INF/classes/'
    cmdList = []
    cmdList.append("sed -i s/'DBIP'/'" + dbIp + "'/g " + configPath + "jdbc.properties")
    cmdList.append("sed -i s/'DBNAME'/'" + dbName + "'/g " + configPath + "jdbc.properties")
    cmdList.append("sed -i s/'DBPWD'/'" + dbPwd + "'/g " + configPath + "jdbc.properties")
    cmdList.append("sed -i s/'MQIP'/'" + mqIp + "'/g " + configPath + "jdbc.properties")
    cmdList.append("sed -i s/'MQPORT'/'" + mqPort + "'/g " + configPath + "jdbc.properties")
    cmdList.append("sed -i s/'MQUSER'/'" + mqUser + "'/g " + configPath + "jdbc.properties")
    cmdList.append("sed -i s/'MQPWD'/'" + mqPwd + "'/g " + configPath + "jdbc.properties")
    exceCmd(cmdList,hostIp,osUser,osPwd,sshPort)


def deployWebProject():
    cmdList = []
    cmdList.append('service tomcat6 stop')
    cmdList.append('rm -fr ' + tomcatDir + "/" + projectName + "*")
    cmdList.append('cp -r ' + distPath + projectName + "/ " + tomcatDir + "/")
    cmdList.append('service tomcat6 start')
    exceCmd(cmdList, hostIp, osUser, osPwd, sshPort)


if __name__ == '__main__':
    init_data()
    print 'hostip:' + hostIp + ' dbIP:' + dbIp + ' mqIp:' + mqIp + ' dbPwd:' + dbPwd + ' osPwd:' + osPwd
    # 修改数据库表
    alterTableStructure()
    # 导入数据
    initTableData()
    initWebApp()
    deployWebProject()
