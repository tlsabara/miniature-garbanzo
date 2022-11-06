from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from assets.models import (
    GarbanzoAssetType,
    GarbanzoAssetItem,
    GarbanzoLinkType,
    GarbanzoAssetClass,
)
from core.models import ExtraField


class ExtraFieldInline(admin.TabularInline):
    model = ExtraField


# Register your models here.
class CustomAssetHistoryAdmin(SimpleHistoryAdmin):
    inlines = [
        ExtraFieldInline,
    ]
    list_display = ("id", "name_item", "status", "user__username")
    history_list_display = ("name_item",)
    history_readonly_fields = (
        "id",
        "name_item",
        "serial_number",
        "asset_number",
        "type_asset",
        "custom_fields",
    )


class CustomGarbanzoAssetAdmin(CustomAssetHistoryAdmin):
    inlines = [
        ExtraFieldInline,
    ]
    history_readonly_fields = (
        "id",
        "name_item",
        "serial_number",
        "tag_number",
        "asset_number",
        "type_asset",
    )

    readonly_fields = ("id",)
    list_display = (
        "name_item",
        "serial_number",
        "asset_number",
        "tag_number",
        "type_asset",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name_item",
                    "serial_number",
                    "tag_number",
                    "type_asset",
                    "asset_number",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name_item",
                    "email",
                    "asset_number",
                    "tag_number",
                    "type_asset",
                    "custom_fields",
                ),
            },
        ),
    )
    search_fields = ("type_asset", "name_item")
    ordering = ("asset_number",)


admin.site.register(GarbanzoAssetItem, CustomGarbanzoAssetAdmin)
admin.site.register(GarbanzoLinkType, SimpleHistoryAdmin)
admin.site.register(GarbanzoAssetType, SimpleHistoryAdmin)
admin.site.register(GarbanzoAssetClass, SimpleHistoryAdmin)
