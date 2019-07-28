from django.db import models
from datetime import datetime

from apps.user.models import UserProfile
from apps.questions.models import QuestionInfo
from apps.paper.models import PaperInfo
from apps.examination.models import ExaminationInfo


# 试卷-试题关联表
class PaperQuestion(models.Model):
    question = models.ForeignKey(QuestionInfo, on_delete=models.CASCADE, verbose_name='试题信息')
    paper = models.ForeignKey(PaperInfo, on_delete=models.CASCADE, verbose_name='试卷信息')
    score = models.FloatField(default=0, verbose_name='题目分数')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(default=datetime.now, auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '试卷-试题关联信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.paper.title, self.question.title)


# 考试-试卷关联表(学生成绩表)
class ReportInfo(models.Model):
    examination = models.ForeignKey(ExaminationInfo, on_delete=models.CASCADE, verbose_name='考试信息')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='考生信息')
    grade = models.FloatField(default=0, verbose_name='学生得分')
    submit_time = models.DateTimeField(default=datetime.now, auto_now=True, verbose_name='提交时间')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '考试-试卷关联信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.examination.title, self.user.username)


# 学生答题表
class AnswerCard(models.Model):
    examination = models.ForeignKey(ExaminationInfo, on_delete=models.CASCADE, verbose_name='考试信息')
    question = models.ForeignKey(QuestionInfo, on_delete=models.CASCADE, verbose_name='试题信息')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='考生信息')
    result = models.BooleanField(default=False, verbose_name='是否正确')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '学生答题信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.examination.title, self.user.username)
