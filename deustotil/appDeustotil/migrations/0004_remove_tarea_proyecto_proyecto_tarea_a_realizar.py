# Generated by Django 4.2 on 2024-05-01 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustotil', '0003_alter_tarea_proyecto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='proyecto',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tarea_a_realizar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appDeustotil.tarea'),
        ),
    ]