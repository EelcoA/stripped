# Generated by Django 3.1.3 on 2020-12-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rm', '0004_auto_20201201_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_nr',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contract',
            name='database_nr',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
