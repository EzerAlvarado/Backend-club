# Generated by Django 5.1.2 on 2025-03-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0015_alter_ordendecompra_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendecompra',
            name='precio_orden',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
