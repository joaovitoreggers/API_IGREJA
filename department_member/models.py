from tabnanny import verbose
from django.db import models
from department.models import Department
from member.models import Member
from tenancy.models import Tenancy

class DepartmentMember(models.Model):
    tenancy = models.ForeignKey(
        Tenancy,
        on_delete=models.CASCADE,
        verbose_name='Igreja: '
    )
    member_id = models.ForeignKey(
        Member,
        on_delete=models.PROTECT,
        verbose_name='Membro: '
    )
    department_id = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        verbose_name='Departamento: '
    )
    entry_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Entrada: '    
    )
    description = models.TextField(
        blank=True,
        null=True,
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

    def __str__(self):
        return f'{self.member_id.name} | {self.department_id.name}'
    
    class Meta:
        verbose_name = 'Membro do Departamento'
        verbose_name_plural = 'Membros do Departamento'