from django.contrib import admin

from relation.models import PaperQuestion, ReportInfo, AnswerCard, SystemCode


@admin.register(PaperQuestion)
class PaperQuestionAdmin(admin.ModelAdmin):
    # 表头显示
    list_display = (
        'question', 'paper', 'score', 'create_time', 'update_time'
    )

    # 支持搜索的字段
    search_fields = (
        'question', 'paper',
    )

    # 支持进入编辑模式的字段
    list_display_links = (
        'question',
    )

    # 分页页数
    list_per_page = 20


@admin.register(ReportInfo)
class ReportInfoAdmin(admin.ModelAdmin):
    # 表头显示
    list_display = (
        'examination', 'user', 'grade', 'submit_time', 'create_time',
    )

    # 支持搜索的字段
    search_fields = (
        'examination', 'user',
    )

    # 支持进入编辑模式的字段
    list_display_links = (
        'examination',
    )

    # 分页页数
    list_per_page = 20


@admin.register(AnswerCard)
class AnswerCardAdmin(admin.ModelAdmin):
    # 表头显示
    list_display = (
        'examination', 'question', 'user', 'result', 'create_time',
    )

    # 支持搜索的字段
    search_fields = (
        'examination', 'question', 'user'
    )

    # 支持进入编辑模式的字段
    list_display_links = (
        'examination',
    )

    # 分页页数
    list_per_page = 20


@admin.register(SystemCode)
class SystemCodeAdmin(admin.ModelAdmin):
    # 表头显示
    list_display = (
        'type', 'name', 'value', 'create_time', 'update_time',
    )

    # 支持搜索的字段
    search_fields = (
        'type', 'name'
    )

    # 支持进入编辑模式的字段
    list_display_links = (
        'name',
    )

    # 分页页数
    list_per_page = 20
