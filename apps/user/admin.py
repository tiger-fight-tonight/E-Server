from django.contrib import admin

from user.models import UserProfile, SubjectInfo


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # 表头显示
    list_display = (
        'user_id', 'username', 'role', 'sign_code', 'birth', 'age', 'mobile', 'gender', 'email', 'school', 'class_name'
    )

    # 支持搜索的字段
    search_fields = (
        'user_id', 'username'
    )

    # 支持进入编辑模式的字段
    list_display_links = (
        'username',
    )

    # 分页页数
    list_per_page = 20


@admin.register(SubjectInfo)
class SubjectInfoAdmin(admin.ModelAdmin):
    # 表头显示
    list_display = (
        'subject_id', 'subject_name', 'create_time', 'update_time',
    )

    # 支持搜索的字段
    search_fields = (
        'subject_name', 'subject_id'
    )

    # 支持进入编辑模式的字段
    list_display_links = (
        'subject_name',
    )

    # 分页页数
    list_per_page = 20
