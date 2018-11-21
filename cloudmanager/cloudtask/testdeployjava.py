#!/usr/bin/python
'''
fabric 1.x

#fab -f testdeployjava.py deploy
from fabric.api import *

env.user = 'root'
env.hosts = ['10.10.203.252', ]
env.passwords = {
    'root@10.10.203.252:22': 'vicloud.1',
}

env.projectDir = 'D:/IdeaProject/cloud-manager'
projectName = 'cloud-manager'
tomcatDir = '/var/lib/tomcat6/webapps'


@runs_once
def buildProject():
    with lcd(env.projectDir):
        local('rm -fr ./target/' + projectName + '.war')
        local('mvn clean package')
        local('mv ./target/' + projectName + '-1.0-SNAPSHOT.war ./target/' + projectName + '.war')


@task
def deploy():
    buildProject()
    run("service tomcat6 stop")
    run('rm -fr ' + tomcatDir + "/" + projectName + "*")
    put(env.projectDir + "/target/" + projectName + ".war", tomcatDir + "/" + projectName + ".war")
    run('service tomcat6 start')
'''

from cmdutil import *
excelocalcmd("ls")