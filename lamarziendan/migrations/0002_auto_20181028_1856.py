# Generated by Django 2.0.4 on 2018-10-28 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lamarziendan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='lamarziendan.Genre', verbose_name='genre'),
        ),
    ]