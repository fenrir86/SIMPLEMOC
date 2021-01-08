# Generated by Django 3.1.4 on 2021-01-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], default=1, verbose_name='Situação'),
        ),
    ]
