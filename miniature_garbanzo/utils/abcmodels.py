import uuid
from django.db import models


class UUIDModel(models.Model):
    """
    Model para a ciração de entidades com uuid, para boas praticas de segurança.
    Estou utilizando também o campo pkid para melhorar a indexação no banco de dados.
    """
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True
