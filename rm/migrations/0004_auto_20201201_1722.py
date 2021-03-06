# Generated by Django 3.1.3 on 2020-12-01 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rm', '0003_auto_20201201_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='nr',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='owner_email',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='owner_phone_nr',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='status',
        ),
        migrations.AddField(
            model_name='contract',
            name='contact_person',
            field=models.CharField(blank=True, max_length=50, verbose_name='Contactpersoon'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contact_person_email',
            field=models.CharField(blank=True, max_length=50, verbose_name='Contactpersoon email'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contact_person_phone_nr',
            field=models.CharField(blank=True, max_length=20, verbose_name='Contactpersoon telnr'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_name',
            field=models.CharField(blank=True, max_length=250, verbose_name='Contract naam'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_nr',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_owner',
            field=models.CharField(blank=True, max_length=50, verbose_name='Contracteigenaar'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_owner_email',
            field=models.CharField(blank=True, max_length=50, verbose_name='Contracteigenaar email'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_owner_phone_nr',
            field=models.CharField(blank=True, max_length=20, verbose_name='Contracteigenaar telnr'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_status',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contract',
            name='contracted_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Gecontracteerde waarde'),
        ),
        migrations.AddField(
            model_name='contract',
            name='database_nr',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contract',
            name='description_contract',
            field=models.CharField(blank=True, max_length=250, verbose_name='Beschrijving contract'),
        ),
        migrations.AddField(
            model_name='contract',
            name='end_date_contract',
            field=models.DateField(blank=True, null=True, verbose_name='Einddatum contract'),
        ),
        migrations.AddField(
            model_name='contract',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=50, verbose_name='Fabrikant'),
        ),
        migrations.AddField(
            model_name='contract',
            name='manufacturer_address',
            field=models.CharField(blank=True, max_length=250, verbose_name='Fabrikant Adres'),
        ),
        migrations.AddField(
            model_name='contract',
            name='manufacturer_kvk_nr',
            field=models.CharField(blank=True, max_length=50, verbose_name='Fabrikant KvK nr'),
        ),
        migrations.AddField(
            model_name='contract',
            name='manufacturer_website',
            field=models.CharField(blank=True, max_length=50, verbose_name='Fabrikant Website'),
        ),
        migrations.AddField(
            model_name='contract',
            name='service_level_manager',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contract',
            name='service_level_manager_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contract',
            name='service_level_manager_2_email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contract',
            name='service_level_manager_2_phone_nr',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='contract',
            name='service_level_manager_email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contract',
            name='service_level_manager_phone_nr',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.CreateModel(
            name='ReceivedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_nr', models.IntegerField()),
                ('field_01', models.CharField(blank=True, max_length=250)),
                ('field_02', models.CharField(blank=True, max_length=250)),
                ('field_03', models.CharField(blank=True, max_length=250)),
                ('field_04', models.CharField(blank=True, max_length=250)),
                ('field_05', models.CharField(blank=True, max_length=250)),
                ('field_06', models.CharField(blank=True, max_length=250)),
                ('field_07', models.CharField(blank=True, max_length=250)),
                ('field_08', models.CharField(blank=True, max_length=250)),
                ('field_09', models.CharField(blank=True, max_length=250)),
                ('field_10', models.CharField(blank=True, max_length=250)),
                ('field_11', models.CharField(blank=True, max_length=250)),
                ('field_12', models.CharField(blank=True, max_length=250)),
                ('field_13', models.CharField(blank=True, max_length=250)),
                ('field_14', models.CharField(blank=True, max_length=250)),
                ('field_15', models.CharField(blank=True, max_length=250)),
                ('field_16', models.CharField(blank=True, max_length=250)),
                ('field_17', models.CharField(blank=True, max_length=250)),
                ('field_18', models.CharField(blank=True, max_length=250)),
                ('field_19', models.CharField(blank=True, max_length=250)),
                ('field_20', models.CharField(blank=True, max_length=250)),
                ('field_21', models.CharField(blank=True, max_length=250)),
                ('field_22', models.CharField(blank=True, max_length=250)),
                ('field_23', models.CharField(blank=True, max_length=250)),
                ('field_24', models.CharField(blank=True, max_length=250)),
                ('field_25', models.CharField(blank=True, max_length=250)),
                ('field_26', models.CharField(blank=True, max_length=250)),
                ('field_27', models.CharField(blank=True, max_length=250)),
                ('field_28', models.CharField(blank=True, max_length=250)),
                ('field_29', models.CharField(blank=True, max_length=250)),
                ('field_30', models.CharField(blank=True, max_length=250)),
                ('field_31', models.CharField(blank=True, max_length=250)),
                ('field_32', models.CharField(blank=True, max_length=250)),
                ('field_33', models.CharField(blank=True, max_length=250)),
                ('field_34', models.CharField(blank=True, max_length=250)),
                ('field_35', models.CharField(blank=True, max_length=250)),
                ('field_36', models.CharField(blank=True, max_length=250)),
                ('field_37', models.CharField(blank=True, max_length=250)),
                ('field_38', models.CharField(blank=True, max_length=250)),
                ('field_39', models.CharField(blank=True, max_length=250)),
                ('field_40', models.CharField(blank=True, max_length=250)),
                ('field_41', models.CharField(blank=True, max_length=250)),
                ('field_42', models.CharField(blank=True, max_length=250)),
                ('field_43', models.CharField(blank=True, max_length=250)),
                ('field_44', models.CharField(blank=True, max_length=250)),
                ('field_45', models.CharField(blank=True, max_length=250)),
                ('field_46', models.CharField(blank=True, max_length=250)),
                ('field_47', models.CharField(blank=True, max_length=250)),
                ('field_48', models.CharField(blank=True, max_length=250)),
                ('field_49', models.CharField(blank=True, max_length=250)),
                ('field_50', models.CharField(blank=True, max_length=250)),
                ('interface_call', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_data', to='rm.interfacecall')),
            ],
        ),
    ]
