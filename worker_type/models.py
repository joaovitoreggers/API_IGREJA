from django.db import models

from tenancy.models import Tenancy

class WorkerType(models.Model):

    tenancy = models.ForeignKey(
        Tenancy,
        on_delete=models.CASCADE,
        verbose_name='Igreja: '
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Nome: '
    )
    description = models.TextField(
        verbose_name='Descrição: '
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Criado em: '
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em: '
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Tipo de Obreiro'
        verbose_name_plural = 'Tipos de Obreiros'

    def __str__(self):
        return f'{self.name}'