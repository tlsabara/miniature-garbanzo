import uuid
from django.db import models
from simple_history.models import HistoricalRecords


class GarbanzoModel(models.Model):
    """
    Model para a ciração de entidades com uuid, para boas praticas de segurança.
    Estou utilizando também o campo pkid para melhorar a indexação no banco de dados.
    """
    # UUID
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    # Campos sistema
    system_create_at = models.DateTimeField(auto_now_add=True)
    system_edited_at = models.DateTimeField(auto_now=True)
    system_history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
