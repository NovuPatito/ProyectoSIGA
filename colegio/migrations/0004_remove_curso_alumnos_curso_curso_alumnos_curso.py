# Generated by Django 5.0.4 on 2024-04-26 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0003_rename_edadalum_alumno_edad_alum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='alumnos_curso',
        ),
        migrations.AddField(
            model_name='curso',
            name='alumnos_curso',
            field=models.ManyToManyField(related_name='alumnoss', to='colegio.alumno'),
        ),
    ]
