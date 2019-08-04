from django.contrib import admin

from paper.models import PaperInfo


@admin.register(PaperInfo)
class PaperInfoAdmin(admin.ModelAdmin):
    # 表头显示
    list_display = (
        'paper_id', 'title', 'degree', 'subject', 'score', 'owner_id', 'creator_id', 'is_public',
        'create_time', 'update_time'
    )

    # 支持搜索的字段
    search_fields = (
        'paper_id', 'title', 'owner_id', 'creator_id'
    )

    # 支持进入编辑模式的字段
    list_display_links = (
        'title',
    )

    # 过滤器
    list_filter = (
        'degree', 'is_public'
    )

    # 分页页数
    list_per_page = 20
