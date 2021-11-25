# Generated by Django 3.2.9 on 2021-11-25 14:29

import ckeditor.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=35, unique=True)),
                ('slug', models.SlugField(max_length=35, unique=True)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=35)),
                ('dificuldade', models.CharField(choices=[(1, 'Fácil'), (2, 'Mediana'), (3, 'Complexo')], max_length=1)),
                ('rendimento', models.PositiveSmallIntegerField(help_text='Nº de porções')),
                ('imagem', models.ImageField(upload_to='')),
                ('ingredientes', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('modo_de_preparo', ckeditor.fields.RichTextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receitas', to='myapp.categoria')),
            ],
        ),
    ]
