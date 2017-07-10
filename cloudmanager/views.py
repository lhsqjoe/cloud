# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from cloudmanager.models import TUser
from cloudmanager.cloudtask.cmdutil import *


# @csrf_protect
def index(request):
    # user = TUser(user_name="zhangsan",is_vaildusb=0)
    # user.save()
    # return HttpResponse("Hello, world. You're at the polls index.")
    resList = exceCmd('10.10.203.162','root','vicloud.1',["virsh list --all| sed -n '3,$p'|awk  '{print $1\",\"$2\",\"$3 $4}'"])
    tempList = resList[0].split('\n')
    vmList = []
    for temp in tempList:
        vm=temp.split(",",-1)
        vmList.append(vm)
    return render(request,"index.html",{'vmList':vmList})



#用户登录页面
def login(request):
    "需要判断用户名密码"
    return render(request,"login.html");