# Generated by Django 2.2.6 on 2019-10-08 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='aprovao',
            new_name='aprovado',
        ),
    ]
