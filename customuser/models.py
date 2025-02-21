from django.db import models
from tenancy.models import Tenancy
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    tenant = models.ForeignKey(
        Tenancy,
        on_delete= models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Tenant:',
        related_name='tenant_user'
    )
    phone_number = models.CharField(
        max_length=20, 
        verbose_name='Número de telefone',
        blank=True,
        null=True
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  
        blank=True
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Usuário Customizado'
        verbose_name = 'Usuários Customizados'

    def __str__(self):
        return f'{self.username}'