from django.db import models

from tenancy.models import Tenancy

class Department(models.Model):

    tenancy = models.ForeignKey(
        Tenancy,
        verbose_name='Igreja: '
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Nome: '
    )
    description = models.TextField(
        verbose_name='Descrição: '
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em: '
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em: '
    )