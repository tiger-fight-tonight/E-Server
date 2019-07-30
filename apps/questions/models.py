import uuid

from django.db import models
from datetime import datetime

from apps.user.models import UserProfile, SubjectInfo


# 试题信息表
class QuestionInfo(models.Model):
    question_id = models.CharField(
        primary_key=True, max_length=50, default=uuid.uuid4(), editable=False, verbose_name='试题ID'
    )
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='试题标题')
    content = models.CharField(max_length=500, null=False, blank=False, verbose_name='试题内容')
    degree = models.IntegerField(default=0, null=False, blank=False, verbose_name='难度')
    subject = models.ForeignKey(SubjectInfo, on_delete=models.CASCADE, verbose_name='课程')
    type = models.IntegerField(default=0, null=False, blank=False, verbose_name='试题类型')
    answer = models.CharField(max_length=20, null=False, blank=False, verbose_name='试题答案')
    analysis = models.CharField(max_length=500, default='', verbose_name='试题解析')
    is_public = models.BooleanField(default=False, verbose_name='是否分享')
    creator_id = models.CharField(max_length=50, null=False, blank=False, verbose_name='创建人')
    owner_id = models.CharField(max_length=50, null=False, blank=False, verbose_name='拥有人')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '试题信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
