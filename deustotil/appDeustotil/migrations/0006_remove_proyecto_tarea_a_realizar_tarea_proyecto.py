# Generated by Django 4.2 on 2024-05-01 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustotil', '0005_alter_proyecto_tarea_a_realizar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='tarea_a_realizar',
        ),
        migrations.AddField(
            model_name='tarea',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appDeustotil.proyecto'),
        ),
    ]
