# Generated by Django 2.0.4 on 2018-10-29 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lamarziendan', '0004_auto_20181029_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='description',
        ),
    ]
