# Generated by Django 2.2.6 on 2019-10-16 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponto_turistico', '0008_pontoturistico_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocIdentificador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptioin', models.CharField(max_length=100)),
            ],
        ),
    ]