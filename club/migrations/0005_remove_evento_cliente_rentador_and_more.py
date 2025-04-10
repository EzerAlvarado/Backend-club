# Generated by Django 5.1.2 on 2025-02-20 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_ordendecompra_listo_a_pagar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='cliente_rentador',
        ),
        migrations.AddField(
            model_name='evento',
            name='correo_rentador',
            field=models.CharField(blank=True, help_text='Correo del cliente que renta', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='nombre_rentador',
            field=models.CharField(blank=True, help_text='Nombre del cliente que renta', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(blank=True, help_text='Nombre del cliente', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_de_cliente',
            field=models.CharField(blank=True, help_text='Tipo de cliente Vip, Frecuente, Nuevo, etc', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='pago_renta',
            field=models.BooleanField(default=True),
        ),
    ]
