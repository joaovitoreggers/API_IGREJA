from django.db import models
from tenancy.models import Tenancy

class Supplier(models.Model):

    tenancy = models.ForeignKey(
        Tenancy,
        on_delete=models.CASCADE,
        verbose_name='Igreja: '
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Nome: '
    )
    cpf_cnpj = models.CharField(
        max_length=18, 
        unique=True,
        verbose_name='CPF ou CNPJ do Fornecedor: '
    )
    adress = models.CharField(
        max_length=255,
        verbose_name='Endereço ou referencial do Fornecedor: '
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Número de Telefone: '
    )
    email = models.CharField(
        max_length=255,
        verbose_name='Email: '
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
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return f'{self.name}'