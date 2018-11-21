# -*- coding: utf-8 -*-
from .cmdutil import *

hostIp = '10.10.203.252'
hostUser = 'root'
hostPwd = 'vicloud.1'


def getVmList():
    resList = exceCmd(hostIp, hostUser, hostPwd,
                      ["virsh list --all| sed -n '3,$p'|awk  '{if($0!=\"\")print $1\",\"$2\",\"$3 $4}'"])
    vmList = resList[0].split('\n', -1)
    return vmList


def closeAllVm(vmList):
    for temp in vmList:
        if '' != temp:
            vm = temp.split(",", -1)
            if (vm[2] == 'running'):
                print('命令virsh destroy ', vm[1])
                exceCmd(hostIp, hostUser, hostPwd, ['virsh destroy ' + vm[1]])


def startAllVm(vmList):
    for temp in vmList:
        if '' != temp:
            vm = temp.split(",", -1)
            if (vm[2] == 'shutoff'):
                print('命令virsh start ', vm[1])
                exceCmd(hostIp, hostUser, hostPwd, ['virsh start ' + vm[1]])


def undefineAllVm(vmList):
    for temp in vmList:
        if '' != temp:
            vm = temp.split(",", -1)
            if (vm[2] == 'shutoff'):
                print('命令virsh undefine ', vm[1])
                exceCmd(hostIp, hostUser, hostPwd, ['virsh undefine ' + vm[1]])


if __name__ == '__main__':
    vmList = getVmList()
    # closeAllVm(vmList)
    # startAllVm(vmList)
