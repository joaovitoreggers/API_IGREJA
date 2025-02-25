from tabnanny import verbose
from django.db import models
from department.models import Department
import tax_document
from tax_document.models import TaxDocument
from tenancy.models import Tenancy

class TypeChoices(models.Choices):
    ENTRY = 'Entrada'
    EXIT = 'Saída'
    DEFAULT = 'Default'


class FiscalTransaction(models.Model):
    tenancy = models.ForeignKey(
        Tenancy,
        on_delete=models.CASCADE,
        verbose_name='Igreja: '
    )
    type = models.CharField(
        max_length=15,
        choices=TypeChoices.choices,
        default=TypeChoices.DEFAULT
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição: '
    )
    value = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Valor da Movimentação: '
    )
    department_id = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        verbose_name='Departamento relacionado a Transação: ',
        blank=True,
        null=True
    )
    tax_document_id = models.ForeignKey(
        TaxDocument,
        on_delete=models.PROTECT,
        verbose_name='Documento Fiscal Relacionado a Transação: ',
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

    def __str__(self):
        if self.department_id is not None:
            return f'{self.department_id} | {self.type} | {self.value}'
        if self.tax_document_id is not None:
            return f'{self.tax_document_id} | {self.type} | {self.value}'
        return f'{self.type} | {self.value}'
    
    class Meta:
        verbose_name = 'Transação Fiscal'
        verbose_name_plural = 'Transações Fiscais'