# Generated by Django 2.2.6 on 2019-10-10 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponto_turistico', '0007_auto_20191008_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]