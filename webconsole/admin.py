from django.contrib import admin
from . import models


# 用户相关
admin.site.register(models.SysUser)
admin.site.register(models.UserRole)
admin.site.register(models.Role)
admin.site.register(models.RolePermissions)
admin.site.register(models.Permissions)

