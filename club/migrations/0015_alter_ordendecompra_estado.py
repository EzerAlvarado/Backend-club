# Generated by Django 5.1.2 on 2025-03-10 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0014_alter_ordendecompra_usuario_responsable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendecompra',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('incluido_en_cargo', 'Incluido en Cargo'), ('pagado', 'Pagado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20),
        ),
    ]
