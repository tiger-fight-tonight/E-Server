from django.contrib import admin

from examination.models import ExaminationInfo


@admin.register(ExaminationInfo)
class PaperInfoAdmin(admin.ModelAdmin):
    # 表头显示
    list_display = (
        'examination_id', 'title', 'paper', 'state', 'start_time', 'end_time', 'min_grade', 'max_grade', 'avg_grade',
        'creator_id', 'create_time', 'update_time'
    )

    # 支持搜索的字段
    search_fields = (
        'examination_id', 'title', 'paper', 'creator_id'
    )

    # 支持进入编辑模式的字段
    list_display_links = (
        'title',
    )

    # 过滤器
    list_filter = ['state']

    # 分页页数
    list_per_page = 20
