# Generated by Django 2.1.7 on 2019-08-11 15:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20190804_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectinfo',
            name='subject_id',
            field=models.CharField(default=uuid.UUID('ed11c2f8-4315-4075-8705-433c592dd83a'), editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='科目ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.CharField(default=uuid.UUID('491bcf68-2b37-49d8-8429-d1a8b0d83bd1'), editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='用户ID'),
        ),
    ]
