# Generated by Django 4.2 on 2024-05-01 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustotil', '0004_remove_tarea_proyecto_proyecto_tarea_a_realizar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='tarea_a_realizar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDeustotil.tarea'),
        ),
    ]
