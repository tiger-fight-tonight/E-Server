import uuid

from django.db import models
from datetime import datetime

from apps.user.models import UserProfile, SubjectInfo


# 试卷信息表
class PaperInfo(models.Model):
    paper_id = models.CharField(
        primary_key=True, max_length=50, default=uuid.uuid4(), editable=False, verbose_name='试卷ID'
    )
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='试卷标题')
    degree = models.IntegerField(default=0, null=False, blank=False, verbose_name='难度')
    subject = models.ForeignKey(SubjectInfo, on_delete=models.CASCADE, verbose_name='课程')
    is_public = models.BooleanField(default=False, verbose_name='是否分享')
    score = models.FloatField(null=False, blank=False, verbose_name='试卷分数')
    creator_id = models.CharField(max_length=50, null=False, blank=False, verbose_name='创建人')
    owner_id = models.CharField(max_length=50, null=False, blank=False, verbose_name='拥有人')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '试卷信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
