# Generated by Django 2.1.7 on 2019-08-04 06:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20190804_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questioninfo',
            name='question_id',
            field=models.CharField(default=uuid.UUID('1899a7b4-43bc-4372-99a2-bc804d2025cc'), editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='试题ID'),
        ),
    ]