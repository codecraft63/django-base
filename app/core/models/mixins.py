from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampMixin(models.Model):
    created_on = models.DateTimeField(_('Created on'), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_('Updated_on'), auto_now=True, editable=False)

    class Meta:
        abstract = True
