# Generated by Django 2.0.4 on 2018-10-28 17:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='naam')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='beschrijving')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='afbeelding')),
                ('links', models.TextField(blank=True, help_text='Plak hier per regel één hyperlink', verbose_name='social media links')),
            ],
            options={
                'verbose_name': 'Artiest',
                'verbose_name_plural': 'Artiesten',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=255, verbose_name='titel')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='beschrijving')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='afbeelding')),
                ('photolink', models.URLField(blank=True, verbose_name='link naar het fotoalbum')),
            ],
            options={
                'verbose_name': 'Editie',
                'verbose_name_plural': 'Edities',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='naam')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(blank=True, verbose_name='nummer')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performances', to='lamarziendan.Artist', verbose_name='artiest')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performances', to='lamarziendan.Edition', verbose_name='editie')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='lamarziendan.Genre', verbose_name='genre')),
            ],
            options={
                'verbose_name': 'Optreden',
                'verbose_name_plural': 'Optredens',
                'ordering': ['number'],
            },
        ),
    ]
