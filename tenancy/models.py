from django.db import models

class Tenancy(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Igreja'
    )
    description = models.TextField(
        verbose_name='Descrição'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado Em: '
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em: '
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Igreja'
        verbose_name_plural = 'Igrejas'
        
    def __str__(self):
        return f'{self.name}'