from django.db import models
from django.utils.translation import gettext_lazy as _

from miniature_garbanzo.utils.abcmodels import GarbanzoModel

from core.utils import AppCoreChoisces


# Create your models here.
class GarbanzoPerms(GarbanzoModel):
    desc_gperms = models.CharField(max_length=100)
    sys_name_gperms = models.CharField(max_length=100)
    long_desc_gperms = models.TextField(max_length=1000, null=True, blank=True)
    app_gperms = models.TextField(
        max_length=50, choices=AppCoreChoisces.GarbanzoPerms.APPS, default="CORE"
    )

    def __str__(self):
        return self.sys_name_gperms


class ExtraFieldType(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name=_("Name"),
    )

    description = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Description"),
    )

    model = models.ForeignKey("assets.GarbanzoAssetType", on_delete=models.DO_NOTHING)

    fixed_values = models.BooleanField(
        default=False,
        verbose_name=_("Fixed values"),
    )

    class Meta:
        ordering = [
            "name",
        ]

    def __unicode__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class ExtraField(models.Model):
    """
    Model to create custom fields.
    :field_type: Connection to the field type.
    :value: Current value of this extra field.
    """

    item = models.ForeignKey(
        "assets.GarbanzoAssetItem",
        verbose_name=_("Asset Item"),
        related_name="extra_fields_instance",
        help_text=_(
            "Only field types with fixed values can be chosen to add" " global values."
        ),
        on_delete=models.DO_NOTHING,
    )

    field_type = models.ForeignKey(
        "ExtraFieldType",
        verbose_name=_("Field type"),
        related_name="extra_fields",
        help_text=_(
            "Only field types with fixed values can be chosen to add" " global values."
        ),
        on_delete=models.DO_NOTHING,
    )

    value = models.CharField(
        max_length=200,
        verbose_name=_("Value"),
    )

    class Meta:
        ordering = [
            "field_type__name",
        ]

    def __unicode__(self):
        return "{0} ({1}) - {2}".format(
            self.field_type,
            self.field_type.get_model_display() or "general",
            self.value,
        )

    def __str__(self):
        return f"{self.field_type} on ASSET: {self.item.asset_number}"
