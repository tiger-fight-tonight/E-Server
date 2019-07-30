import uuid

from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# 用户基本信息
class UserProfile(AbstractUser):
    user_id = models.CharField(
        primary_key=True, max_length=50, default=uuid.uuid4(), editable=False, verbose_name='用户ID'
    )
    sign_code = models.CharField(max_length=20, default='', verbose_name='职工号/学号')
    gender = models.IntegerField(default=0, verbose_name='性别')
    role = models.IntegerField(default=0, verbose_name='用户类型')
    age = models.IntegerField(default=18, verbose_name='年龄')
    birth = models.DateField(null=True, blank=True, verbose_name='生日')
    mobile = models.CharField(max_length=11, default='', null=True, blank=True, verbose_name='电话号码')
    school = models.CharField(max_length=50, default='', verbose_name='学校')
    class_name = models.CharField(max_length=50, default='', verbose_name='班级')
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=200, verbose_name='头像')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 课程信息表
class SubjectInfo(models.Model):
    subject_id = models.CharField(
        primary_key=True, max_length=50, default=uuid.uuid4(), editable=False, verbose_name='科目ID'
    )
    subject_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='科目名称')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '科目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject_name
