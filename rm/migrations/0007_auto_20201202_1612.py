# Generated by Django 3.1.3 on 2020-12-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rm', '0006_interfacecall_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfacecall',
            name='status',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='interfacecall',
            name='type',
            field=models.CharField(max_length=15),
        ),
    ]
