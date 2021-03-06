# Generated by Django 4.0.4 on 2022-05-15 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0005_remove_prescripcion_comprimidos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescripcion',
            name='comprimidos',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prescripcion',
            name='dias_tratamiento',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prescripcion',
            name='frecuencia_hrs',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prescripcion',
            name='medicamento',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='farmacia.medicamento'),
        ),
        migrations.DeleteModel(
            name='ListaMedicamentos',
        ),
    ]
