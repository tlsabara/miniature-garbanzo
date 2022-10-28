from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
from core.models import GarbanzoPerms, ExtraFieldType, ExtraField


class CustomGarbanzoPermsAdmin(SimpleHistoryAdmin):
    list_display = ('sys_name_gperms', 'app_gperms', 'desc_gperms', 'system_active')
    list_filter = ('app_gperms',)
    ordering = ('app_gperms', 'sys_name_gperms',)


admin.site.register(GarbanzoPerms, CustomGarbanzoPermsAdmin)
admin.site.register(ExtraFieldType, admin.ModelAdmin)
