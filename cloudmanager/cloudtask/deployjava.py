#!/usr/bin/python
# fab -f deployjava.py deploy
from fabric.api import *

env.user = 'root'
env.hosts = ['10.10.203.162', ]
env.passwords = {
    'root@10.10.203.162:22': 'vicloud.1',
}

env.workDir = '/root/deploynew'
projectName = 'cloud-manager'
tomcatDir = '/var/lib/tomcat6/webapps'
svnUrl = 'svn://10.10.200.5/cloud/10cloudclassroom/code/bs/cloud-manager'
svnCodeVersion = '2264'
svnUserName = 'liuzhanqiao'
svnPwd = 'liuzhanqiao7u8i9o0p'

# DataBase
dbIp = '10.10.203.162'
dbName = 'vcloud'
dbPwd = 'vicloud.1'
# rabbitMQ
mqIp = '10.10.203.162'
mqPort = '5672'
mqUser = 'guest'
mqPwd = 'eucalyptus'


@runs_once
def buildProject():
    with lcd(env.workDir + '/'):
        local('rm -fr '+projectName+'*')
        local('svn co ' + svnUrl + ' -r ' + svnCodeVersion + '  --username ' + svnUserName + ' --password ' + svnPwd)
    with lcd(env.workDir + '/' + projectName + '/src/main/resources'):
        local("sed -i s/'DBIP'/'" + dbIp + "'/g jdbc.properties")
        local("sed -i s/'DBNAME'/'" + dbName + "'/g jdbc.properties")
        local("sed -i s/'DBPWD'/'" + dbPwd + "'/g jdbc.properties")
        local("sed -i s/'MQIP'/'" + mqIp + "'/g jdbc.properties")
        local("sed -i s/'MQPORT'/'" + mqPort + "'/g jdbc.properties")
        local("sed -i s/'MQUSER'/'" + mqUser + "'/g jdbc.properties")
        local("sed -i s/'MQPWD'/'" + mqPwd + "'/g jdbc.properties")
    with lcd(env.workDir + '/' + projectName):
        local('rm -fr ./target/' + projectName + '.war')
        local('mvn clean package')
        local('mv ./target/' + projectName + '-1.0-SNAPSHOT.war ./target/' + projectName + '.war')


@task
def deploy():
    buildProject()
    run("service tomcat6 stop")
    run('rm -fr ' + tomcatDir + "/" + projectName + "*")
    put(env.workDir+"/"+projectName + "/target/" + projectName + ".war", tomcatDir + "/" + projectName + ".war")
    run('service tomcat6 start')
