# Generated by Django 3.0.5 on 2020-05-12 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_auto_20200427_1443'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
