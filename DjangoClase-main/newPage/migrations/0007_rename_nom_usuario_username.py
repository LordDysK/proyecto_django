# Generated by Django 4.1.3 on 2023-06-30 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newPage', '0006_alter_usuario_activo_alter_usuario_fechanacimiento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Nom',
            new_name='username',
        ),
    ]
