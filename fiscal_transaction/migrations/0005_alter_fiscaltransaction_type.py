# Generated by Django 5.1.6 on 2025-02-26 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiscal_transaction', '0004_alter_fiscaltransaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiscaltransaction',
            name='type',
            field=models.CharField(choices=[('Entrada', 'Entry'), ('Saída', 'Exit'), ('Default', 'Default')], default='Default', max_length=15),
        ),
    ]
