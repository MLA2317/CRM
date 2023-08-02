from django.contrib import admin

from .models import TeamGroup


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'direction', 'teacher', 'room', 'updated_at', 'created_at', 'is_active')
    filter_horizontal = ('students',)
    list_filter = ('updated_at', 'created_at', 'is_active')
    readonly_fields = ('updated_at', 'created_at')


admin.site.register(TeamGroup, TeamAdmin)
