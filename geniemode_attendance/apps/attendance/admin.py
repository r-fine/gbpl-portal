from django.contrib import admin

from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """Admin View for Attendance"""

    list_display = ("user", "day", "date", "is_present", "status", "remarks")
    list_filter = ("date", "user")
    readonly_fields = ("created_at",)
    search_fields = ("user",)
    list_editable = ("is_present", "status", "remarks")
    list_per_page = 25
