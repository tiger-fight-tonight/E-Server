# Generated by Django 2.1.7 on 2019-07-30 14:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExaminationInfo',
            fields=[
                ('examination_id', models.CharField(default=uuid.UUID('cbdfdd8c-c966-45c6-aa1d-78cf58d5a59f'), editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='考试ID')),
                ('title', models.CharField(max_length=50, verbose_name='考试标题')),
                ('start_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='考试开始时间')),
                ('end_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='考试结束时间')),
                ('min_grade', models.FloatField(default=0, verbose_name='最低分')),
                ('max_grade', models.FloatField(default=0, verbose_name='最高分')),
                ('avg_grade', models.FloatField(default=0, verbose_name='平均分')),
                ('state', models.IntegerField(default=0, verbose_name='考试状态')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paper.PaperInfo', verbose_name='试卷')),
            ],
            options={
                'verbose_name': '考试信息',
                'verbose_name_plural': '考试信息',
            },
        ),
    ]
