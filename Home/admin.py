from django.contrib import admin
from .models import MonitorTask

# Register your models here.


class MonitorTaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['task_name']}),
        (None,               {'fields': ['task_host']}),
        (None,               {'fields': ['task_status']}),
    ]
    list_display = ('task_name', 'task_host', 'task_status')
    list_filter = ['task_host', 'task_status']
    search_fields = ['task_host', 'task_name', 'task_status']


admin.site.register(MonitorTask, MonitorTaskAdmin)
