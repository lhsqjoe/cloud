# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import *

#用户模块
admin.site.register(TUser)
admin.site.register(TRole)
admin.site.register(TUserRole)
admin.site.register(TRolePermission)
admin.site.register(TMenu)

#虚拟机相关
admin.site.register(TInstance)
