from logging.config import valid_ident
from math import fabs
from django.db import models
import tenancy
from tenancy.models import Tenancy
from worker_type.models import WorkerType

class Member(models.Model):

    tenancy = models.ForeignKey(
        Tenancy,
        on_delete=models.CASCADE,
        verbose_name='Igreja: '
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Nome: '
    )
    bithday_date = models.DateTimeField(
        verbose_name='Data de Aniversário: '
    )
    adress = models.CharField(
        max_length=255,
        verbose_name='Endereço: '
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Número de Telefone: '
    )
    email = models.CharField(
        max_length=255,
        verbose_name='Email: '
    )
    batism_date = models.DateTimeField(
        verbose_name='Data de Batismo: '
    )
    is_worker = models.BooleanField(
        default=False,
        verbose_name='É obreiro? '
    )
    worker_type = models.ForeignKey(
        WorkerType,
        verbose_name='Classificação de Obreiro; ',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em: '
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em: '
    )


    class Meta:
        ordering = ['id']
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'

    def __str__(self):
        return f'{self.name}'
    
class Contribution(models.Model):
    tenancy = models.ForeignKey(
        Tenancy,
        verbose_name='Igreja: ',
        on_delete=models.CASCADE
    )
    member_id = models.ForeignKey(
        Member,
        on_delete=models.PROTECT,
        verbose_name='Membro contrinuinte: '
    )
    value = models.DecimalField(
        decimal_places=2,
        max_digits=20,
        verbose_name='Valor da Contribuição: '
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em: '  
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em: '
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Contribuição: '
        verbose_name_plural = 'Contribuições: '

    def __str__(self):
        return f'{self.member_id.name} | {self.value}'