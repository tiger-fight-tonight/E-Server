import uuid

from django.db import models
from datetime import datetime

from user.models import UserProfile
from paper.models import PaperInfo


# 考试信息表
class ExaminationInfo(models.Model):
    examination_id = models.CharField(
        primary_key=True, max_length=50, default=uuid.uuid4(), editable=False, verbose_name='考试ID'
    )
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='考试标题')
    paper = models.ForeignKey(PaperInfo, on_delete=models.CASCADE, verbose_name='试卷')
    start_time = models.DateTimeField(default=datetime.now, verbose_name='考试开始时间')
    end_time = models.DateTimeField(default=datetime.now, verbose_name='考试结束时间')
    min_grade = models.FloatField(default=0, verbose_name='最低分')
    max_grade = models.FloatField(default=0, verbose_name='最高分')
    avg_grade = models.FloatField(default=0, verbose_name='平均分')
    state = models.IntegerField(default=0, null=False, blank=False, verbose_name='考试状态')
    creator_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='创建人')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '考试信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
