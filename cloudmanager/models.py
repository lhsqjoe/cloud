# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TAnnouncement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    size = models.CharField(db_column='SIZE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=40, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=50)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    expiretime = models.DateTimeField(db_column='EXPIRETIME', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_ANNOUNCEMENT'


class TBackupLink(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instance_num = models.CharField(db_column='INSTANCE_NUM', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    link_relation = models.TextField(db_column='LINK_RELATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_BACKUP_LINK'


class TBackupRules(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200)  # Field name made lowercase.
    descript = models.CharField(db_column='DESCRIPT', max_length=2000, blank=True,
                                null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='NUMBER', blank=True, null=True)  # Field name made lowercase.
    rule_exp = models.CharField(db_column='RULE_EXP', max_length=2000, blank=True,
                                null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=16, blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='CAPACITY', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(db_column='LEVEL', blank=True, null=True)  # Field name made lowercase.
    is_customer = models.IntegerField(db_column='IS_CUSTOMER', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    model = models.IntegerField(db_column='MODEL', blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=64, blank=True,
                                 null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    terminate_time = models.DateTimeField(db_column='TERMINATE_TIME', blank=True,
                                          null=True)  # Field name made lowercase.
    num_of_units = models.IntegerField(db_column='NUM_OF_UNITS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_BACKUP_RULES'


class TBackupRulesUserRel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instance_num = models.CharField(db_column='INSTANCE_NUM', max_length=11, blank=True,
                                    null=True)  # Field name made lowercase.
    backup_rules_id = models.IntegerField(db_column='BACKUP_RULES_ID', blank=True,
                                          null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    owner_id = models.IntegerField(db_column='OWNER_ID', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_BACKUP_RULES_USER_REL'


class TBlListen(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nsid = models.IntegerField(db_column='NSID', blank=True, null=True)  # Field name made lowercase.
    pub_port = models.IntegerField(db_column='PUB_PORT', blank=True, null=True)  # Field name made lowercase.
    mode = models.CharField(db_column='MODE', max_length=64, blank=True, null=True)  # Field name made lowercase.
    balance = models.CharField(db_column='BALANCE', max_length=64, blank=True, null=True)  # Field name made lowercase.
    check_inter = models.IntegerField(db_column='CHECK_INTER', blank=True, null=True)  # Field name made lowercase.
    check_timeout = models.IntegerField(db_column='CHECK_TIMEOUT', blank=True, null=True)  # Field name made lowercase.
    check_mode = models.CharField(db_column='CHECK_MODE', max_length=16, blank=True,
                                  null=True)  # Field name made lowercase.
    cookies = models.IntegerField(db_column='COOKIES', blank=True, null=True)  # Field name made lowercase.
    forwardfor = models.IntegerField(db_column='FORWARDFOR', blank=True, null=True)  # Field name made lowercase.
    usesrc = models.IntegerField(db_column='USESRC', blank=True, null=True)  # Field name made lowercase.
    dontlognull = models.IntegerField(db_column='DONTLOGNULL', blank=True, null=True)  # Field name made lowercase.
    redispatch = models.IntegerField(db_column='REDISPATCH', blank=True, null=True)  # Field name made lowercase.
    check_uri = models.CharField(db_column='CHECK_URI', max_length=256, blank=True,
                                 null=True)  # Field name made lowercase.
    stats_refresh = models.IntegerField(db_column='STATS_REFRESH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_BL_LISTEN'


class TBlMember(models.Model):
    listen_id = models.IntegerField(db_column='LISTEN_ID', blank=True, null=True)  # Field name made lowercase.
    pri_ip = models.CharField(db_column='PRI_IP', max_length=64, blank=True, null=True)  # Field name made lowercase.
    pri_port = models.IntegerField(db_column='PRI_PORT', blank=True, null=True)  # Field name made lowercase.
    server_name = models.CharField(db_column='SERVER_NAME', max_length=64, blank=True,
                                   null=True)  # Field name made lowercase.
    weithg = models.IntegerField(db_column='WEITHG', blank=True, null=True)  # Field name made lowercase.
    rise = models.IntegerField(db_column='RISE', blank=True, null=True)  # Field name made lowercase.
    fall = models.IntegerField(db_column='FALL', blank=True, null=True)  # Field name made lowercase.
    maxconn = models.IntegerField(db_column='MAXCONN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_BL_MEMBER'


class TBootRules(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200)  # Field name made lowercase.
    descript = models.CharField(db_column='DESCRIPT', max_length=2000, blank=True,
                                null=True)  # Field name made lowercase.
    rule_exp = models.CharField(db_column='RULE_EXP', max_length=2000, blank=True,
                                null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=16, blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='OWNER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=2000, blank=True,
                                 null=True)  # Field name made lowercase.
    instancenum = models.CharField(db_column='INSTANCENUM', max_length=2000, blank=True,
                                   null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_BOOT_RULES'


class TBox(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    netmask = models.CharField(db_column='NETMASK', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    instance_num = models.CharField(db_column='INSTANCE_NUM', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    instance_name = models.CharField(db_column='INSTANCE_NAME', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    classroom_id = models.IntegerField(db_column='CLASSROOM_ID', blank=True, null=True)  # Field name made lowercase.
    broadcast_flag = models.IntegerField(db_column='BROADCAST_FLAG', blank=True,
                                         null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME')  # Field name made lowercase.
    software_version = models.CharField(db_column='SOFTWARE_VERSION', max_length=20, blank=True,
                                        null=True)  # Field name made lowercase.
    upgradestatus = models.CharField(db_column='UPGRADESTATUS', max_length=20, blank=True,
                                     null=True)  # Field name made lowercase.
    heartflag = models.CharField(db_column='HEARTFLAG', max_length=10, blank=True,
                                 null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cpuinfo = models.CharField(db_column='CPUINFO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memeryinfo = models.CharField(db_column='MEMERYINFO', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    usbstate = models.CharField(db_column='USBSTATE', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_BOX'


class TBoxheart(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_BOXHEART'


class TCc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cc_id = models.CharField(db_column='CC_ID', max_length=36)  # Field name made lowercase.
    cc_name = models.CharField(db_column='CC_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=36)  # Field name made lowercase.
    clc_id = models.CharField(db_column='CLC_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    cc_value = models.CharField(db_column='CC_VALUE', unique=True, max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    cc_remark = models.CharField(db_column='CC_REMARK', max_length=500, blank=True,
                                 null=True)  # Field name made lowercase.
    nfs_id = models.CharField(db_column='NFS_ID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    price_disk = models.IntegerField(db_column='PRICE_DISK', blank=True, null=True)  # Field name made lowercase.
    price_brandwidth = models.IntegerField(db_column='PRICE_BRANDWIDTH', blank=True,
                                           null=True)  # Field name made lowercase.
    price_cpu = models.IntegerField(db_column='PRICE_CPU', blank=True, null=True)  # Field name made lowercase.
    price_memory = models.IntegerField(db_column='PRICE_MEMORY', blank=True, null=True)  # Field name made lowercase.
    root_pwd = models.CharField(db_column='ROOT_PWD', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    sys_store_flag = models.IntegerField(db_column='SYS_STORE_FLAG', blank=True,
                                         null=True)  # Field name made lowercase.
    sys_store_path = models.IntegerField(db_column='SYS_STORE_PATH', blank=True,
                                         null=True)  # Field name made lowercase.
    data_store_flag = models.IntegerField(db_column='DATA_STORE_FLAG', blank=True,
                                          null=True)  # Field name made lowercase.
    data_store_path = models.IntegerField(db_column='DATA_STORE_PATH', blank=True,
                                          null=True)  # Field name made lowercase.
    backup_store_flag = models.IntegerField(db_column='BACKUP_STORE_FLAG', blank=True,
                                            null=True)  # Field name made lowercase.
    backup_store_path = models.IntegerField(db_column='BACKUP_STORE_PATH', blank=True,
                                            null=True)  # Field name made lowercase.
    dc_id = models.IntegerField(db_column='DC_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_CC'


class TCcPort(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cc_ip = models.CharField(db_column='CC_IP', max_length=36)  # Field name made lowercase.
    port = models.IntegerField(db_column='PORT')  # Field name made lowercase.
    is_vaild = models.IntegerField(db_column='IS_VAILD')  # Field name made lowercase.
    instance_num = models.CharField(db_column='INSTANCE_NUM', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    cc_id = models.CharField(db_column='CC_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_CC_PORT'


class TClassroom(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    cur_courses = models.IntegerField(db_column='CUR_COURSES', blank=True, null=True)  # Field name made lowercase.
    cur_user = models.CharField(db_column='CUR_USER', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sign_time = models.CharField(db_column='SIGN_TIME', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_CLASSROOM'


class TCmdinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cmdtype = models.CharField(db_column='CMDTYPE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cmdstr = models.CharField(db_column='CMDSTR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_CMDINFO'


class TCompany(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='PID', blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='COMPANYNAME', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    businesscategory = models.CharField(db_column='BUSINESSCATEGORY', max_length=20, blank=True,
                                        null=True)  # Field name made lowercase.
    companyaddress = models.CharField(db_column='COMPANYADDRESS', max_length=60, blank=True,
                                      null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.
    createpeople = models.CharField(db_column='CREATEPEOPLE', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=30, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_COMPANY'


class TConfig(models.Model):
    cname = models.CharField(unique=True, max_length=255)
    cvalue = models.CharField(max_length=255)
    cremark = models.CharField(max_length=255, blank=True, null=True)
    showflag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_CONFIG'


class TCooperation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    cuid = models.IntegerField(db_column='CUID', blank=True, null=True)  # Field name made lowercase.
    instancenum = models.CharField(db_column='INSTANCENUM', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    cootype = models.CharField(db_column='COOTYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_COOPERATION'


class TCourses(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    courses_name = models.CharField(db_column='COURSES_NAME', max_length=60, blank=True,
                                    null=True)  # Field name made lowercase.
    backup_num = models.CharField(db_column='BACKUP_NUM', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    instance_num = models.CharField(db_column='INSTANCE_NUM', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    img_name = models.CharField(db_column='IMG_NAME', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    valid = models.IntegerField(db_column='VALID', blank=True, null=True)  # Field name made lowercase.
    courses_size = models.FloatField(db_column='COURSES_SIZE', blank=True, null=True)  # Field name made lowercase.
    courses_path = models.CharField(db_column='COURSES_PATH', max_length=140, blank=True,
                                    null=True)  # Field name made lowercase.
    courses_default = models.IntegerField(db_column='COURSES_DEFAULT', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_COURSES'


class TCourseClassRel(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    courses_id = models.BigIntegerField(db_column='COURSES_ID', blank=True, null=True)  # Field name made lowercase.
    classroom_id = models.BigIntegerField(db_column='CLASSROOM_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_COURSE_CLASS_REL'


class TDatahigh(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    serverip = models.CharField(db_column='SERVERIP', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    standbyip = models.CharField(db_column='STANDBYIP', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    port = models.CharField(db_column='PORT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_DATAHIGH'


class TDc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dcname = models.CharField(db_column='DCNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dcflag = models.CharField(db_column='DCFLAG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstdns = models.CharField(db_column='FIRSTDNS', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    secdns = models.CharField(db_column='SECDNS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_DC'


class TDepartment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    company_id = models.IntegerField(db_column='COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='COMPANY_NAME', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    department_id = models.IntegerField(db_column='DEPARTMENT_ID', blank=True, null=True)  # Field name made lowercase.
    department_name = models.CharField(db_column='DEPARTMENT_NAME', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    departmentpeople = models.CharField(db_column='DEPARTMENTPEOPLE', max_length=40, blank=True,
                                        null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_DEPARTMENT'


class TDhcp(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    start_ip = models.CharField(db_column='START_IP', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    end_ip = models.CharField(db_column='END_IP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pool_id = models.BigIntegerField(db_column='POOL_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_DHCP'


class TDiskMnt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mount_point = models.CharField(db_column='MOUNT_POINT', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='FLAG', blank=True, null=True)  # Field name made lowercase.
    cc_id = models.CharField(db_column='CC_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    cc_ip = models.CharField(db_column='CC_IP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    instance_id = models.CharField(db_column='INSTANCE_ID', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    volume_identify = models.CharField(db_column='VOLUME_IDENTIFY', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_DISK_MNT'


class TInstance(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instance_num = models.CharField(db_column='INSTANCE_NUM', unique=True, max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    vm_owner = models.CharField(db_column='VM_OWNER', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    vm_style_id = models.BigIntegerField(db_column='VM_STYLE_ID', blank=True, null=True)  # Field name made lowercase.
    vm_image_id = models.BigIntegerField(db_column='VM_IMAGE_ID', blank=True, null=True)  # Field name made lowercase.
    private_ip = models.CharField(db_column='PRIVATE_IP', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    public_ip = models.CharField(db_column='PUBLIC_IP', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    nc_ip = models.CharField(db_column='NC_IP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    port = models.CharField(db_column='PORT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vncport = models.CharField(db_column='VNCPORT', max_length=11, blank=True, null=True)  # Field name made lowercase.
    vm_password = models.CharField(db_column='VM_PASSWORD', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    terminate_time = models.DateTimeField(db_column='TERMINATE_TIME', blank=True,
                                          null=True)  # Field name made lowercase.
    ramdisk_id = models.CharField(db_column='RAMDISK_ID', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    kernel_id = models.CharField(db_column='KERNEL_ID', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    machine_id = models.CharField(db_column='MACHINE_ID', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    vm_style_name = models.CharField(db_column='VM_STYLE_NAME', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    cluster = models.CharField(db_column='CLUSTER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valid = models.IntegerField(db_column='VALID', blank=True, null=True)  # Field name made lowercase.
    instance_name = models.CharField(db_column='INSTANCE_NAME', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    cpu = models.IntegerField(db_column='CPU', blank=True, null=True)  # Field name made lowercase.
    memory = models.IntegerField(db_column='MEMORY', blank=True, null=True)  # Field name made lowercase.
    disk = models.IntegerField(db_column='DISK', blank=True, null=True)  # Field name made lowercase.
    nc_id = models.CharField(db_column='NC_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    host_name = models.CharField(db_column='HOST_NAME', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    gateway = models.CharField(db_column='GATEWAY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    netmask = models.CharField(db_column='NETMASK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dns = models.CharField(db_column='DNS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    brandwidth = models.IntegerField(db_column='BRANDWIDTH', blank=True, null=True)  # Field name made lowercase.
    validate_time = models.DateTimeField(db_column='VALIDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=500, blank=True, null=True)  # Field name made lowercase.
    agent_flag = models.CharField(db_column='AGENT_FLAG', max_length=10, blank=True,
                                  null=True)  # Field name made lowercase.
    agent_first_flag = models.IntegerField(db_column='AGENT_FIRST_FLAG', blank=True,
                                           null=True)  # Field name made lowercase.
    vlan_id = models.IntegerField(db_column='VLAN_ID', blank=True, null=True)  # Field name made lowercase.
    rdp_port = models.CharField(db_column='RDP_PORT', max_length=6)  # Field name made lowercase.
    order_detail_id = models.IntegerField(db_column='ORDER_DETAIL_ID', blank=True,
                                          null=True)  # Field name made lowercase.
    vm_creater = models.CharField(db_column='VM_CREATER', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    agent_name = models.CharField(db_column='AGENT_NAME', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    emipath = models.CharField(db_column='emiPath', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sg_id = models.BigIntegerField(db_column='SG_ID', blank=True, null=True)  # Field name made lowercase.
    current_bk_link = models.BigIntegerField(db_column='CURRENT_BK_LINK', blank=True,
                                             null=True)  # Field name made lowercase.
    ippool_id = models.BigIntegerField(db_column='IPPOOL_ID', blank=True, null=True)  # Field name made lowercase.
    task_id = models.IntegerField(db_column='TASK_ID', blank=True, null=True)  # Field name made lowercase.
    base_bk_complete = models.IntegerField(db_column='BASE_BK_COMPLETE', blank=True,
                                           null=True)  # Field name made lowercase.
    classroom_id = models.BigIntegerField(db_column='CLASSROOM_ID', blank=True, null=True)  # Field name made lowercase.
    template_machine_flag = models.IntegerField(db_column='TEMPLATE_MACHINE_FLAG', blank=True,
                                                null=True)  # Field name made lowercase.
    machine_use_flag = models.IntegerField(db_column='MACHINE_USE_FLAG', blank=True,
                                           null=True)  # Field name made lowercase.
    sign_time = models.CharField(db_column='SIGN_TIME', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    screenshot_flag = models.IntegerField(db_column='SCREENSHOT_FLAG', blank=True,
                                          null=True)  # Field name made lowercase.
    ha_flag = models.IntegerField(db_column='HA_FLAG', blank=True, null=True)  # Field name made lowercase.
    power_flag = models.IntegerField(db_column='POWER_FLAG', blank=True, null=True)  # Field name made lowercase.
    power_id = models.CharField(db_column='POWER_ID', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    resolution = models.CharField(db_column='RESOLUTION', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    desktop_num = models.CharField(db_column='DESKTOP_NUM', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_INSTANCE'


class TIp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dns = models.CharField(db_column='DNS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    netmark = models.CharField(db_column='NETMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gateway = models.CharField(db_column='GATEWAY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    vlan_id = models.IntegerField(db_column='VLAN_ID', blank=True, null=True)  # Field name made lowercase.
    cc_id = models.CharField(db_column='CC_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    pool_id = models.IntegerField(db_column='POOL_ID', blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='USER', max_length=64, blank=True, null=True)  # Field name made lowercase.
    valid = models.IntegerField(db_column='VALID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_IP'


class TIpPool(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pool_id = models.IntegerField(db_column='POOL_ID', blank=True, null=True)  # Field name made lowercase.
    net_node_id = models.CharField(db_column='NET_NODE_ID', max_length=64, blank=True,
                                   null=True)  # Field name made lowercase.
    pool_type = models.IntegerField(db_column='POOL_TYPE', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=256, blank=True, null=True)  # Field name made lowercase.
    vlan_id = models.IntegerField(db_column='VLAN_ID', blank=True, null=True)  # Field name made lowercase.
    mask = models.CharField(db_column='MASK', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gateway = models.CharField(db_column='GATEWAY', max_length=15, blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    pool_value = models.CharField(db_column='POOL_VALUE', max_length=36, blank=True,
                                  null=True)  # Field name made lowercase.
    network_number = models.CharField(db_column='NETWORK_NUMBER', max_length=18, blank=True,
                                      null=True)  # Field name made lowercase.
    dns = models.CharField(db_column='DNS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_ip = models.CharField(db_column='START_IP', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    end_ip = models.CharField(db_column='END_IP', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_IP_POOL'


class TIssuedRules(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200)  # Field name made lowercase.
    descript = models.CharField(db_column='DESCRIPT', max_length=2000, blank=True,
                                null=True)  # Field name made lowercase.
    rule_exp = models.CharField(db_column='RULE_EXP', max_length=2000, blank=True,
                                null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=16, blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='OWNER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=2000, blank=True,
                                 null=True)  # Field name made lowercase.
    instancenum = models.CharField(db_column='INSTANCENUM', max_length=2000, blank=True,
                                   null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_ISSUED_RULES'


class TLoginfo(models.Model):
    user_id = models.CharField(max_length=32, blank=True, null=True)
    user_ip = models.CharField(max_length=80, blank=True, null=True)
    class_path = models.CharField(max_length=256, blank=True, null=True)
    class_method = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField()
    loglevel = models.CharField(db_column='LogLevel', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    message = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_LOGINFO'


class TMenu(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    leaf = models.IntegerField()
    url = models.CharField(max_length=1000, blank=True, null=True)
    iconskin = models.CharField(max_length=64, blank=True, null=True)
    target = models.CharField(max_length=100, blank=True, null=True)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    sn = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'T_MENU'


class TMeruser(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    allowhost = models.CharField(db_column='ALLOWHOST', max_length=45, blank=True,
                                 null=True)  # Field name made lowercase.
    merchant = models.CharField(db_column='MERCHANT', max_length=30, blank=True,
                                null=True)  # Field name made lowercase.
    md5key = models.CharField(db_column='MD5KEY', max_length=96, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_MERUSER'


class TMigrate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instance_id = models.CharField(db_column='INSTANCE_ID', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    cc_id = models.CharField(db_column='CC_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    before_nc = models.CharField(db_column='BEFORE_NC', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    after_nc = models.CharField(db_column='AFTER_NC', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    migrate_time = models.DateTimeField(db_column='MIGRATE_TIME')  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_MIGRATE'


class TMonitor(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instance_num = models.CharField(db_column='INSTANCE_NUM', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    used_cpu = models.IntegerField(db_column='USED_CPU', blank=True, null=True)  # Field name made lowercase.
    vda_rd = models.CharField(db_column='VDA_RD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vda_wr = models.CharField(db_column='VDA_WR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vm_owner = models.CharField(db_column='VM_OWNER', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_MONITOR'


class TMsg(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    msg_sender = models.CharField(db_column='MSG_SENDER', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    msg_receiver = models.CharField(db_column='MSG_RECEIVER', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    msg_title = models.CharField(db_column='MSG_TITLE', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    msg_content = models.CharField(db_column='MSG_CONTENT', max_length=500, blank=True,
                                   null=True)  # Field name made lowercase.
    msg_date = models.DateTimeField(db_column='MSG_DATE')  # Field name made lowercase.
    instance_num = models.CharField(db_column='INSTANCE_NUM', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    read_flag = models.IntegerField(db_column='READ_FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_MSG'


class TNc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nc_id = models.CharField(db_column='NC_ID', max_length=36)  # Field name made lowercase.
    nc_name = models.CharField(db_column='NC_NAME', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=36)  # Field name made lowercase.
    cc_id = models.CharField(db_column='CC_ID', max_length=36)  # Field name made lowercase.
    tcp_port = models.CharField(db_column='TCP_PORT', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    disk_url = models.CharField(db_column='DISK_URL', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    ha_flag = models.IntegerField(db_column='HA_FLAG', blank=True, null=True)  # Field name made lowercase.
    monitor_flag = models.IntegerField(db_column='MONITOR_FLAG', blank=True, null=True)  # Field name made lowercase.
    root_pwd = models.CharField(db_column='ROOT_PWD', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    sys_store_id = models.IntegerField(db_column='SYS_STORE_ID', blank=True, null=True)  # Field name made lowercase.
    data_store_id = models.IntegerField(db_column='DATA_STORE_ID', blank=True, null=True)  # Field name made lowercase.
    backup_store_id = models.IntegerField(db_column='BACKUP_STORE_ID', blank=True,
                                          null=True)  # Field name made lowercase.
    screenshot_id = models.IntegerField(db_column='SCREENSHOT_ID', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_NC'


class TNetNode(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    net_node_id = models.CharField(db_column='NET_NODE_ID', max_length=64, blank=True,
                                   null=True)  # Field name made lowercase.
    net_node_ip = models.CharField(db_column='NET_NODE_IP', max_length=64, blank=True,
                                   null=True)  # Field name made lowercase.
    cc_id = models.CharField(db_column='CC_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=256, blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    default_flag = models.IntegerField(db_column='DEFAULT_FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_NET_NODE'


class TNetService(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=16, blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='USER', max_length=64, blank=True, null=True)  # Field name made lowercase.
    net_node_id = models.CharField(db_column='NET_NODE_ID', max_length=64, blank=True,
                                   null=True)  # Field name made lowercase.
    service_name = models.CharField(db_column='SERVICE_NAME', max_length=64, blank=True,
                                    null=True)  # Field name made lowercase.
    pub_ip = models.CharField(db_column='PUB_IP', max_length=64, blank=True, null=True)  # Field name made lowercase.
    pub_port = models.IntegerField(db_column='PUB_PORT', blank=True, null=True)  # Field name made lowercase.
    pri_ip = models.CharField(db_column='PRI_IP', max_length=64, blank=True, null=True)  # Field name made lowercase.
    instance_num = models.CharField(db_column='INSTANCE_NUM', max_length=60, blank=True,
                                    null=True)  # Field name made lowercase.
    log_name = models.CharField(db_column='LOG_NAME', max_length=128, blank=True,
                                null=True)  # Field name made lowercase.
    maxconn = models.IntegerField(db_column='MAXCONN', blank=True, null=True)  # Field name made lowercase.
    con_timeout = models.IntegerField(db_column='CON_TIMEOUT', blank=True, null=True)  # Field name made lowercase.
    retries = models.IntegerField(db_column='RETRIES', blank=True, null=True)  # Field name made lowercase.
    nbproc = models.IntegerField(db_column='NBPROC', blank=True, null=True)  # Field name made lowercase.
    daemon = models.IntegerField(db_column='DAEMON', blank=True, null=True)  # Field name made lowercase.
    mode = models.CharField(db_column='MODE', max_length=16, blank=True, null=True)  # Field name made lowercase.
    stats_refresh = models.IntegerField(db_column='STATS_REFRESH', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_NET_SERVICE'


class TNfs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nfs_id = models.CharField(db_column='NFS_ID', unique=True, max_length=36, blank=True,
                              null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=36, blank=True, null=True)  # Field name made lowercase.
    dictionary = models.CharField(db_column='DICTIONARY', max_length=128, blank=True,
                                  null=True)  # Field name made lowercase.
    sizeg = models.CharField(db_column='SIZEG', max_length=11, blank=True, null=True)  # Field name made lowercase.
    cc_id = models.CharField(db_column='CC_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    purpose = models.CharField(db_column='PURPOSE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usedsize = models.CharField(db_column='USEDSIZE', max_length=11, blank=True,
                                null=True)  # Field name made lowercase.
    usedratio = models.CharField(db_column='USEDRATIO', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_NFS'


class TOperLog(models.Model):
    action = models.CharField(max_length=32, blank=True, null=True)
    logname = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'T_OPER_LOG'


class TOrg(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='PID', blank=True, null=True)  # Field name made lowercase.
    orgname = models.CharField(db_column='ORGNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    businesscategory = models.CharField(db_column='BUSINESSCATEGORY', max_length=20, blank=True,
                                        null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=60, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.
    createpeople = models.CharField(db_column='CREATEPEOPLE', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=30, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_ORG'


class TOs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    system_name = models.CharField(db_column='SYSTEM_NAME', max_length=60)  # Field name made lowercase.
    system_size = models.FloatField(db_column='SYSTEM_SIZE')  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    system_path = models.CharField(db_column='SYSTEM_PATH', max_length=60, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_OS'


class TPlatform(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    serverip = models.CharField(db_column='SERVERIP', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    standbyip = models.CharField(db_column='STANDBYIP', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    port = models.CharField(db_column='PORT', max_length=80, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_PLATFORM'


class TQuartz(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    job_code = models.CharField(db_column='JOB_CODE', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    job_name = models.CharField(db_column='JOB_NAME', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    job_class = models.CharField(db_column='JOB_CLASS', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    job_frequency = models.CharField(db_column='JOB_FREQUENCY', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    params = models.CharField(db_column='PARAMS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_QUARTZ'


class TRole(models.Model):
    name = models.CharField(max_length=100)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'T_ROLE'


class TRolePermission(models.Model):
    permission_id = models.IntegerField()
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_ROLE_PERMISSION'


class TScreenshot(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instance_num = models.CharField(db_column='INSTANCE_NUM', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    create_time = models.DateField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(db_column='FILE_NAME', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    thumbfile_name = models.CharField(db_column='THUMBFILE_NAME', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_SCREENSHOT'


class TSecurityGroup(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_id = models.BigIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    default_flag = models.IntegerField(db_column='DEFAULT_FLAG', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_SECURITY_GROUP'


class TSecurityGroupRules(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    security_group_id = models.BigIntegerField(db_column='SECURITY_GROUP_ID', blank=True,
                                               null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rule = models.CharField(db_column='RULE', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    protocol = models.CharField(db_column='PROTOCOL', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    start_port = models.CharField(db_column='START_PORT', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    end_port = models.CharField(db_column='END_PORT', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    direction = models.IntegerField(db_column='DIRECTION', blank=True, null=True)  # Field name made lowercase.
    operation = models.IntegerField(db_column='OPERATION', blank=True, null=True)  # Field name made lowercase.
    source_ip = models.CharField(db_column='SOURCE_IP', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    dest_ip = models.CharField(db_column='DEST_IP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_SECURITY_GROUP_RULES'


class TSharespace(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sname = models.CharField(db_column='SNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    totalsize = models.CharField(db_column='ToTALSIZE', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    usedsize = models.CharField(db_column='USEDSIZE', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    usepercent = models.CharField(db_column='USEPERCENT', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    rootpwd = models.CharField(db_column='ROOTPWD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcid = models.IntegerField(db_column='DCID', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_SHARESPACE'


class TSharespaceuser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    sharename = models.CharField(db_column='SHARENAME', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    pwd = models.CharField(db_column='PWD', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_SHARESPACEUSER'


class TShutdownRules(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200)  # Field name made lowercase.
    descript = models.CharField(db_column='DESCRIPT', max_length=2000, blank=True,
                                null=True)  # Field name made lowercase.
    rule_exp = models.CharField(db_column='RULE_EXP', max_length=2000, blank=True,
                                null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=16, blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='OWNER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=2000, blank=True,
                                 null=True)  # Field name made lowercase.
    instancenum = models.CharField(db_column='INSTANCENUM', max_length=2000, blank=True,
                                   null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_SHUTDOWN_RULES'


class TSnapshotInfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    instance_num = models.CharField(db_column='INSTANCE_NUM', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    file_num = models.CharField(db_column='FILE_NUM', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    snapshot_num = models.CharField(db_column='SNAPSHOT_NUM', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    user = models.CharField(db_column='USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valid = models.IntegerField(db_column='VALID', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='FLAG', blank=True, null=True)  # Field name made lowercase.
    is_use = models.IntegerField(db_column='IS_USE', blank=True, null=True)  # Field name made lowercase.
    creater = models.CharField(db_column='CREATER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    backup_link_id = models.IntegerField(db_column='BACKUP_LINK_ID', blank=True,
                                         null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_SNAPSHOT_INFO'


class TStackUrl(models.Model):
    code = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64, blank=True, null=True)
    req_action = models.CharField(max_length=16)
    url = models.CharField(max_length=256)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_STACK_URL'


class TStore(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    business_style = models.IntegerField(db_column='BUSINESS_STYLE', blank=True,
                                         null=True)  # Field name made lowercase.
    store_style = models.IntegerField(db_column='STORE_STYLE', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='PATH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nfs_id = models.IntegerField(db_column='NFS_ID', blank=True, null=True)  # Field name made lowercase.
    sizeg = models.CharField(db_column='SIZEG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usedsize = models.CharField(db_column='USEDSIZE', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    usedratio = models.CharField(db_column='USEDRATIO', max_length=10, blank=True,
                                 null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_STORE'


class TTerminalControl(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=60, blank=True, null=True)  # Field name made lowercase.
    access = models.CharField(db_column='ACCESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_TERMINAL_CONTROL'


class TUkeyv(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    keya = models.CharField(db_column='KEYA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    keyb = models.CharField(db_column='KEYB', max_length=20, blank=True, null=True)  # Field name made lowercase.
    keyc = models.CharField(db_column='KEYC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    keyd = models.CharField(db_column='KEYD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    keye = models.CharField(db_column='KEYE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_UKEYV'


class TUser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    is_agent = models.IntegerField(db_column='IS_AGENT', blank=True, null=True)  # Field name made lowercase.
    is_admin = models.IntegerField(db_column='IS_ADMIN', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    certificate_type = models.IntegerField(db_column='CERTIFICATE_TYPE', blank=True,
                                           null=True)  # Field name made lowercase.
    certificate_no = models.IntegerField(db_column='CERTIFICATE_NO', blank=True,
                                         null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    query_key = models.CharField(db_column='QUERY_KEY', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    secury_key = models.CharField(db_column='SECURY_KEY', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    is_vaildusb = models.IntegerField(db_column='IS_VAILDUSB')  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    validkey = models.CharField(max_length=64, blank=True, null=True)
    postcode = models.CharField(max_length=6, blank=True, null=True)
    company = models.CharField(max_length=128, blank=True, null=True)
    regcode = models.CharField(max_length=64, blank=True, null=True)
    user_creater = models.CharField(db_column='USER_CREATER', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    usertype = models.IntegerField(blank=True, null=True)
    depid = models.IntegerField(db_column='DEPID', blank=True, null=True)  # Field name made lowercase.
    orgid = models.IntegerField(db_column='ORGID', blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='COMPANYID', blank=True, null=True)  # Field name made lowercase.
    secdepid = models.IntegerField(db_column='SECDEPID', blank=True, null=True)  # Field name made lowercase.
    sflag = models.IntegerField(db_column='SFLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_USER'


class TUserRole(models.Model):
    user_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'T_USER_ROLE'


class TVmApplicationMain(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    vm_style = models.CharField(db_column='VM_STYLE', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    descinfo = models.CharField(db_column='DESCINFO', max_length=500, blank=True,
                                null=True)  # Field name made lowercase.
    vm_id = models.BigIntegerField(db_column='VM_ID', blank=True, null=True)  # Field name made lowercase.
    vm_instance_num = models.CharField(db_column='VM_INSTANCE_NUM', max_length=100, blank=True,
                                       null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    pay_flag = models.IntegerField(db_column='PAY_FLAG', blank=True, null=True)  # Field name made lowercase.
    cpu = models.IntegerField(db_column='CPU', blank=True, null=True)  # Field name made lowercase.
    memory = models.IntegerField(db_column='MEMORY', blank=True, null=True)  # Field name made lowercase.
    disk = models.IntegerField(db_column='DISK', blank=True, null=True)  # Field name made lowercase.
    emi = models.CharField(db_column='EMI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    order_id = models.CharField(db_column='ORDER_ID', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    validity_time = models.DateTimeField(db_column='VALIDITY_TIME', blank=True, null=True)  # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    brandwidth = models.IntegerField(db_column='BRANDWIDTH', blank=True, null=True)  # Field name made lowercase.
    vm_name = models.CharField(db_column='VM_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='CATEGORY', blank=True, null=True)  # Field name made lowercase.
    available_zone = models.CharField(db_column='AVAILABLE_ZONE', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
    runinstance_flag = models.IntegerField(db_column='RUNINSTANCE_FLAG', blank=True,
                                           null=True)  # Field name made lowercase.
    duration = models.IntegerField(blank=True, null=True)
    price_paied = models.IntegerField(db_column='PRICE_PAIED', blank=True, null=True)  # Field name made lowercase.
    order_source = models.CharField(db_column='ORDER_SOURCE', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    mount = models.IntegerField(db_column='MOUNT', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notify_flag = models.IntegerField(db_column='NOTIFY_FLAG', blank=True, null=True)  # Field name made lowercase.
    deliver_info = models.CharField(db_column='DELIVER_INFO', max_length=200, blank=True,
                                    null=True)  # Field name made lowercase.
    vm_creater = models.CharField(db_column='VM_CREATER', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    powervm_flag = models.IntegerField(db_column='POWERVM_FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_VM_APPLICATION_MAIN'


class TVmImage(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image_name = models.CharField(db_column='IMAGE_NAME', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    image_identify = models.CharField(db_column='IMAGE_IDENTIFY', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
    vm_style_id = models.BigIntegerField(db_column='VM_STYLE_ID', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='PATH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bukkit = models.CharField(db_column='BUKKIT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prefix = models.CharField(db_column='PREFIX', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    image_owner = models.CharField(db_column='IMAGE_OWNER', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    public_status = models.CharField(db_column='PUBLIC_STATUS', max_length=20, blank=True,
                                     null=True)  # Field name made lowercase.
    architecture = models.CharField(db_column='ARCHITECTURE', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    image_type = models.CharField(db_column='IMAGE_TYPE', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    kernel_identity = models.CharField(db_column='KERNEL_IDENTITY', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    ramdisk_identity = models.CharField(db_column='RAMDISK_IDENTITY', max_length=50, blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_VM_IMAGE'


class TVmImageRela(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image_identify = models.CharField(db_column='IMAGE_IDENTIFY', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
    image_owner = models.CharField(db_column='IMAGE_OWNER', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_VM_IMAGE_RELA'


class TVolumeInfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    volume_identify = models.CharField(db_column='VOLUME_IDENTIFY', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    volume_name = models.CharField(db_column='VOLUME_NAME', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='SIZE', blank=True, null=True)  # Field name made lowercase.
    islocal = models.CharField(db_column='ISLOCAL', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=11, blank=True, null=True)  # Field name made lowercase.
    bind_time = models.DateTimeField(db_column='BIND_TIME')  # Field name made lowercase.
    instance_id = models.CharField(db_column='INSTANCE_ID', max_length=20)  # Field name made lowercase.
    mont_point = models.CharField(db_column='MONT_POINT', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    create_person = models.CharField(db_column='CREATE_PERSON', max_length=20, blank=True,
                                     null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    valid = models.IntegerField(db_column='VALID', blank=True, null=True)  # Field name made lowercase.
    vm_owner = models.CharField(db_column='VM_OWNER', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_VOLUME_INFO'
