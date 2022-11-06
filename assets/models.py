from django.db import models
from django.utils.translation import gettext_lazy as _
from miniature_garbanzo.utils.abcmodels import GarbanzoModel


# Create your models here.
class GarbanzoLinkType(GarbanzoModel):
    desc_garbazno_link = models.CharField(max_length=100)

    def __str__(self):
        return self.desc_garbazno_link


class GarbanzoAssetClass(GarbanzoModel):
    desc_asset_class = models.CharField(max_length=100)
    accepted_links = models.ManyToManyField(
        GarbanzoLinkType,
    )

    def __str__(self):
        return self.desc_asset_class


class GarbanzoAssetType(GarbanzoModel):
    desc_asset_type = models.CharField(max_length=100)
    asset_type_class = models.ForeignKey(
        GarbanzoAssetClass,
        on_delete=models.DO_NOTHING,
        related_name="asset_type_class",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.desc_asset_type


class GarbanzoAssetItem(GarbanzoModel):
    name_item = models.CharField(max_length=100)
    asset_number = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    tag_number = models.CharField(max_length=100)
    type_asset = models.ForeignKey(
        GarbanzoAssetType,
        on_delete=models.DO_NOTHING,
    )
    custom_fields = models.ManyToManyField(
        "core.ExtraField",
        verbose_name=_("Extra fields"),
        limit_choices_to={"field_type__model": type_asset},
    )

    def __str__(self):
        return f"({self.type_asset}) - {self.name_item} - ASSET:{self.asset_number} "
