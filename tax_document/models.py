from django.db import models

from tenancy.models import Tenancy

class DocumentType(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Tipo de Documento'
    )
    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Código de Verificação'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
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
        return self.name
    
    class Meta:
        verbose_name = "Tipo de Documento Fiscal"
        verbose_name_plural = "Tipos de Documentos Fiscais"


class TaxDocument(models.Model):
    tenancy = models.ForeignKey(
        Tenancy,
        on_delete=models.CASCADE,
        verbose_name='Igreja'
    )
    document_number = models.CharField(
        max_length=80,
        verbose_name='Número do Documento'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data do Documento'
    )
    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.CASCADE,
        related_name='Documentos',
        verbose_name='Tipo de Documentos'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )
    file = models.FileField(
        upload_to='documents/',
        blank=True,
        null=True,
        verbose_name='Arquivo em Anexo'
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
        return self.document_number
    
    class Meta:
        verbose_name = 'Documento Fiscal'
        verbose_name_plural = 'Documentos Fiscais'