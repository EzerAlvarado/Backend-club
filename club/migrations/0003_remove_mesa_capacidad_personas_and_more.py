# Generated by Django 5.1.2 on 2025-02-10 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_ordendecompra_completado_cargo_ordendecompra_cargo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesa',
            name='capacidad_personas',
        ),
        migrations.AddField(
            model_name='ordendecompra',
            name='precio_orden',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='fecha_cobro',
            field=models.DateTimeField(null=True),
        ),
    ]
