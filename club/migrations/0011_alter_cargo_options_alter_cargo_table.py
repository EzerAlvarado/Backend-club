# Generated by Django 5.1.2 on 2025-03-09 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0010_alter_usuario_estado_solicitud'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo',
            options={'ordering': ['pk'], 'permissions': [['autorizar_cargo', 'Puede Autorizar Cargos'], ['viewcrud_cargo', 'Puede Visualizar Cargos en el menú']], 'verbose_name': 'Cargo', 'verbose_name_plural': 'Cargos'},
        ),
        migrations.AlterModelTable(
            name='cargo',
            table='cargps',
        ),
    ]
