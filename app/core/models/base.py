import uuid

from django.db import models

from app.core.models.mixins import TimestampMixin


class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class ModelWithTimestamp(TimestampMixin, Model):
    class Meta:
        abstract = True
