# -*- coding: utf-8 -*-
import paramiko

# 远程命令执行工具类
port = 22

"""
    hosname 主机IP username 用户名 password 密码 cmdStr 命令字符串
"""
def exceCmd(hostname, username, password,cmdList):
    paramiko.util.log_to_file('syslogin.log')
    trans = paramiko.Transport((hostname, port))
    trans.connect(username=username, password=password)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh._transport = trans
    resList=[]
    for cmdStr in cmdList:
        stdin, stdout, stderr = ssh.exec_command(cmdStr)
        resStr = stdout.read().decode()
        # print(resStr)
        resList.append(resStr)
    trans.close()
    return resList



if __name__ == '__main__':
    resList = exceCmd('10.10.203.162','root', 'vicloud.1', ['ls -al', 'uname -r'])
    for str in resList:
        print "命令执行结果::",str

