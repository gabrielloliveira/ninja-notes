import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedUUIDModel(models.Model):
    """
    Uma classe de model abstrata que fornece campos para data de criação,
    data de atualização e uuid.
    """

    created_at = models.DateTimeField(_("criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("atualizado em"), auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class Note(TimeStampedUUIDModel):
    title = models.CharField(_("título"), max_length=255)
    content = models.TextField(_("conteúdo"), blank=True, null=True)

    class Meta:
        verbose_name = _("Nota")
        verbose_name_plural = _("Notas")

    def __str__(self):
        return self.title
