# Generated by Django 2.2.6 on 2019-10-14 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_atracao_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='observacoes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
