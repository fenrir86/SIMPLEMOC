# Generated by Django 3.1.4 on 2021-01-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210105_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='alter_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de Alteração'),
        ),
    ]
