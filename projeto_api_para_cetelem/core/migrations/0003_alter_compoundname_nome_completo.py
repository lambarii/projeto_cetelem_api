# Generated by Django 3.2.5 on 2021-07-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_compoundname_nome_completo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compoundname',
            name='nome_completo',
            field=models.CharField(max_length=50),
        ),
    ]
