
from datetime import datetime
from django.db import models
class Model_INCAR(models.Model): #创建INCAR表
    """INCAR表"""
    parameter = models.CharField(verbose_name='参数',max_length=32,blank=True,null=True)
    value = models.CharField(verbose_name="数值",max_length=32,default=0)

class POSCAR_Down(models.Model):
    title = models.CharField(max_length=200,verbose_name=u"文件名称")
    file = models.FileField(upload_to='POSCAR_download/',verbose_name=u"文件添加时间")
    add_time = models.DateTimeField(default=datetime.now(),verbose_name=u"文件添加时间")

# class Model_POSCAR(models.Model):
#     """部门表"""
#     parameter = models.CharField(verbose_name='参数',max_length=32,blank=True,null=True)
#     value = models.CharField(verbose_name="数值",max_length=32,default=0)

# #class UserInfo(models.Model):
#     """员工表"""
#     name = models.CharField(verbose_name="姓名",max_length=16)
#     password = models.CharField(verbose_name="密码",max_length=64)
#     age = models.IntegerField(verbose_name="年龄")
#     account = models.DecimalField(verbose_name="账户余额",max_digits=10,
#                                   decimal_places=2,default=0)
#     create_time = models.DateTimeField(verbose_name="入职时间")
#
#     #无约束
#     # depart_id = models.BigIntegerField(verbose_name = "部门id")
#
#     # 1、有约束
#     # - to ,与哪张表关联
#     # - to_field,表中的那一列关联
#     # 2、django自动
#     # - 写的depart
#     # - 生成数据列 depart_id
#     # 级联删除
#     depart = models.ForeignKey(to = "Department",to_field="id",on_delete = models.CASCADE)
#     # 级联置空
#     # depart = models.ForeignKey(to = "Department",
#     #                            to_field="id",
#     #                            null=True,blank=True,
#     #                            on_delete=models.SET_NULL)
#
#     #在django中做的约束
#     gender_choices = (
#         (1,"男"),
#         (2,"女")
#     )
#     gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices)