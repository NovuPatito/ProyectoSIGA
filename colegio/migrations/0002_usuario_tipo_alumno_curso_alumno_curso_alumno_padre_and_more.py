# Generated by Django 5.0.4 on 2024-04-25 04:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo',
            field=models.TextField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_alum', models.TextField(max_length=50)),
                ('edadalum', models.IntegerField()),
                ('usuario_profe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.TextField(max_length=50)),
                ('alumnos_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.alumno')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso_alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.curso'),
        ),
        migrations.CreateModel(
            name='Padre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_padre', models.TextField(max_length=50)),
                ('edad_padre', models.IntegerField()),
                ('email_padre', models.TextField(max_length=50)),
                ('hijo', models.ManyToManyField(related_name='padres', to='colegio.alumno')),
                ('usuario_padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_profe', models.TextField(max_length=50)),
                ('edad_profe', models.IntegerField()),
                ('email_profe', models.TextField(max_length=50)),
                ('usuario_profe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.profesor'),
        ),
    ]
