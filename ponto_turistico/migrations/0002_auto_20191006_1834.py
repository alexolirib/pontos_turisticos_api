# Generated by Django 2.2.6 on 2019-10-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponto_turistico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]
