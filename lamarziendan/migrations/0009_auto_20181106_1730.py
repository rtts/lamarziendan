# Generated by Django 2.0.4 on 2018-11-06 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lamarziendan', '0008_auto_20181029_1748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participation',
            options={'ordering': ['team_member__name'], 'verbose_name': 'Participatie', 'verbose_name_plural': 'Participaties'},
        ),
        migrations.RemoveField(
            model_name='participation',
            name='number',
        ),
    ]