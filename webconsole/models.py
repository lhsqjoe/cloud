from django.db import models


class SysUser(models.Model):  # 用户表
    username = models.CharField(max_length=200)
    passwd = models.CharField(max_length=50)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    status = models.IntegerField(default=1)  # 1 可用 0 不可用
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.username


class UserRole(models.Model):  # 用户角色表
    user_id = models.IntegerField()
    role_id = models.IntegerField()
    create_time = models.DateTimeField()


class Role(models.Model):  # 角色表
    role_name = models.CharField(max_length=50)
    create_time = models.DateTimeField()


class RolePermissions(models.Model):  # 角色权限表
    role_id = models.IntegerField()
    permissions_id = models.IntegerField()
    create_time = models.DateTimeField()


class Permissions(models.Model):  # 权限表 ,包含菜单
    pid = models.IntegerField()  # 父ID
    permissions_name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    icon_skin = models.CharField(max_length=100)  # 菜单图标
    is_menu = models.IntegerField()  # 1.左侧菜单项
    order_num = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

