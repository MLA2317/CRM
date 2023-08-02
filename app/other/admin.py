from django.contrib import admin
from .models import Profession, Room, DayName, WhereCome, Course, Advertising


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration', 'payment', 'lesson_duration', 'updated_at', 'created_at', 'is_active')
    search_fields = ('id', 'title')
    list_filter = ('updated_at', 'created_at')


# class WhereComeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'student', 'advertising', 'is_active', 'created_at')


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'id')


admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Room)
admin.site.register(DayName)
admin.site.register(Advertising)
admin.site.register(WhereCome,)
admin.site.register(Course, CourseAdmin)

